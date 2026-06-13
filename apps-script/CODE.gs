/**
 * ☕ 咖啡時光廊 CMS — Google Apps Script 後端
 * 
 * 功能：提供故事的新增、讀取、修改、刪除 (CRUD) API
 * 前台：GitHub Pages 透過 gviz 端點讀取 Google Sheet
 * 後台：本 Apps Script Web App 提供管理介面
 * 
 * 部署方式：
 * 1. 在 Google Sheet 中開啟「擴充功能 → Apps Script」
 * 2. 將此檔案內容貼入 Code.gs
 * 3. 新增 HTML 檔案 admin-ui.html，貼入後台介面程式碼
 * 4. 點選「部署 → 新增部署作業 → 網路應用程式」
 *    - 執行身分：我自己
 *    - 存取權限：只有我自己
 * 5. 點擊部署，取得後台 CMS 網址
 */

// ==================== 設定 ====================

// CMS 欄位定義 (對應 Google Sheet 的 A~M 欄)
const HEADERS = [
  'id',         // A: 唯一編號
  'status',     // B: published / draft
  'sort',       // C: 排序權重 (數字越小越前面)
  'category',   // D: 分類主題
  'tag',        // E: 顯示標籤 (例如 Vol.01 愛)
  'title',      // F: 故事標題
  'cover',      // G: 封面圖網址
  'excerpt',    // H: 卡片摘要
  'type',       // I: 媒體類型 (video / audio / text)
  'mediaUrl',   // J: 影音直連網址
  'text',       // K: 故事全文
  'externalLink', // L: 外部連結 (故事主人的家)
  'updatedAt'   // M: 最後更新時間
];

// 分類選項
const CATEGORIES = ['愛', '饒恕', '等候', '盼望', '平安', '恩典', '陪伴', '感恩', '重新開始', '回家'];

// ==================== Web App 入口 ====================

/**
 * GET 請求入口 — 回傳後台管理介面 HTML
 */
function doGet() {
  return HtmlService.createHtmlOutputFromFile('admin-ui')
    .setTitle('☕ 咖啡時光廊 CMS')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// ==================== 取得資料表 ====================

/**
 * 取得工作表（使用第一個工作表）
 */
function getSheet_() {
  return SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
}

// ==================== CRUD 操作 ====================

/**
 * 讀取所有故事（含草稿），回傳 JSON 陣列
 */
function getStories() {
  const sheet = getSheet_();
  const lastRow = sheet.getLastRow();
  
  if (lastRow <= 1) return []; // 只有標題列或空表
  
  const data = sheet.getRange(2, 1, lastRow - 1, HEADERS.length).getValues();
  const stories = [];
  
  for (let i = 0; i < data.length; i++) {
    const row = data[i];
    if (!row[0] && !row[5]) continue; // 跳過完全空白列
    
    const story = {};
    HEADERS.forEach((key, idx) => {
      story[key] = row[idx] !== undefined && row[idx] !== null ? String(row[idx]) : '';
    });
    stories.push(story);
  }
  
  // 依排序欄位升序
  stories.sort((a, b) => (parseInt(a.sort) || 999) - (parseInt(b.sort) || 999));
  
  return stories;
}

/**
 * 新增一篇故事
 * @param {Object} storyData - 故事資料物件
 * @returns {Object} { success: boolean, id: number }
 */
function addStory(storyData) {
  try {
    const sheet = getSheet_();
    const nextId = getNextId_();
    const now = Utilities.formatDate(new Date(), 'Asia/Taipei', 'yyyy-MM-dd HH:mm:ss');
    
    const row = [
      nextId,
      storyData.status || 'draft',
      parseInt(storyData.sort) || 999,
      storyData.category || '',
      storyData.tag || '',
      storyData.title || '（未命名故事）',
      storyData.cover || '',
      storyData.excerpt || '',
      storyData.type || 'text',
      storyData.mediaUrl || '',
      storyData.text || '',
      storyData.externalLink || '',
      now
    ];
    
    sheet.appendRow(row);
    SpreadsheetApp.flush();
    
    return { success: true, id: nextId, message: '故事已新增！' };
  } catch (e) {
    return { success: false, error: e.message };
  }
}

/**
 * 更新一篇故事
 * @param {string|number} id - 故事 ID
 * @param {Object} storyData - 更新後的故事資料
 * @returns {Object} { success: boolean }
 */
function updateStory(id, storyData) {
  try {
    const sheet = getSheet_();
    const rowIndex = findRowById_(id);
    
    if (rowIndex === -1) {
      return { success: false, error: '找不到 ID: ' + id };
    }
    
    const now = Utilities.formatDate(new Date(), 'Asia/Taipei', 'yyyy-MM-dd HH:mm:ss');
    
    const row = [
      parseInt(id),
      storyData.status || 'draft',
      parseInt(storyData.sort) || 999,
      storyData.category || '',
      storyData.tag || '',
      storyData.title || '',
      storyData.cover || '',
      storyData.excerpt || '',
      storyData.type || 'text',
      storyData.mediaUrl || '',
      storyData.text || '',
      storyData.externalLink || '',
      now
    ];
    
    // 自動擴充欄位 (如果 Google Sheet 欄數不夠)
    if (sheet.getMaxColumns() < row.length) {
      sheet.insertColumnsAfter(sheet.getMaxColumns(), row.length - sheet.getMaxColumns());
    }
    
    sheet.getRange(rowIndex, 1, 1, row.length).setValues([row]);
    SpreadsheetApp.flush();
    
    return { success: true, message: '故事已更新！' };
  } catch (e) {
    return { success: false, error: e.message };
  }
}

/**
 * 刪除一篇故事
 * @param {string|number} id - 故事 ID
 * @returns {Object} { success: boolean }
 */
function deleteStory(id) {
  try {
    const sheet = getSheet_();
    const rowIndex = findRowById_(id);
    
    if (rowIndex === -1) {
      return { success: false, error: '找不到 ID: ' + id };
    }
    
    sheet.deleteRow(rowIndex);
    SpreadsheetApp.flush();
    
    return { success: true, message: '故事已刪除！' };
  } catch (e) {
    return { success: false, error: e.message };
  }
}

/**
 * 切換故事上架/下架狀態
 * @param {string|number} id - 故事 ID
 * @returns {Object} { success: boolean, newStatus: string }
 */
function toggleStatus(id) {
  try {
    const sheet = getSheet_();
    const rowIndex = findRowById_(id);
    
    if (rowIndex === -1) {
      return { success: false, error: '找不到 ID: ' + id };
    }
    
    const currentStatus = String(sheet.getRange(rowIndex, 2).getValue()).trim();
    const newStatus = currentStatus === 'published' ? 'draft' : 'published';
    
    sheet.getRange(rowIndex, 2).setValue(newStatus);
    
    // 同步更新時間戳
    const now = Utilities.formatDate(new Date(), 'Asia/Taipei', 'yyyy-MM-dd HH:mm:ss');
    sheet.getRange(rowIndex, 12).setValue(now);
    
    SpreadsheetApp.flush();
    
    return { success: true, newStatus: newStatus, message: newStatus === 'published' ? '已上架！' : '已下架！' };
  } catch (e) {
    return { success: false, error: e.message };
  }
}

/**
 * 取得分類選項清單
 */
function getCategoryOptions() {
  return CATEGORIES;
}

// ==================== 初始化 ====================

/**
 * 初始化工作表 — 建立標題列
 * 第一次使用時執行，或在 Apps Script 編輯器中手動執行
 */
function initializeSheet() {
  const sheet = getSheet_();
  const firstRow = sheet.getRange(1, 1, 1, HEADERS.length).getValues()[0];
  
  // 檢查是否已有標題列
  const hasHeaders = firstRow[0] === 'id' || firstRow[0] === 'ID';
  
  if (!hasHeaders) {
    // 如果第一列有資料，先插入一列
    if (firstRow.some(cell => cell !== '')) {
      sheet.insertRowBefore(1);
    }
    
    // 寫入標題列
    sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);
    
    // 美化標題列
    const headerRange = sheet.getRange(1, 1, 1, HEADERS.length);
    headerRange.setFontWeight('bold');
    headerRange.setBackground('#f4e3cc');
    headerRange.setFontColor('#2a1810');
    headerRange.setHorizontalAlignment('center');
    
    // 凍結標題列
    sheet.setFrozenRows(1);
    
    // 設定欄寬
    sheet.setColumnWidth(1, 50);   // id
    sheet.setColumnWidth(2, 90);   // status
    sheet.setColumnWidth(3, 60);   // sort
    sheet.setColumnWidth(4, 80);   // category
    sheet.setColumnWidth(5, 120);  // tag
    sheet.setColumnWidth(6, 200);  // title
    sheet.setColumnWidth(7, 250);  // cover
    sheet.setColumnWidth(8, 200);  // excerpt
    sheet.setColumnWidth(9, 70);   // type
    sheet.setColumnWidth(10, 250); // mediaUrl
    sheet.setColumnWidth(11, 400); // text
    sheet.setColumnWidth(12, 160); // updatedAt
  }
  
  return { success: true, message: '工作表標題列已就緒！' };
}

// ==================== 內部工具函式 ====================

/**
 * 依 ID 查找列號 (1-indexed，含標題列)
 * @param {string|number} id
 * @returns {number} 列號，找不到回傳 -1
 */
function findRowById_(id) {
  const sheet = getSheet_();
  const lastRow = sheet.getLastRow();
  if (lastRow <= 1) return -1;
  
  const ids = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  
  for (let i = 0; i < ids.length; i++) {
    if (String(ids[i][0]).trim() === String(id).trim()) {
      return i + 2; // +2 因為跳過標題列且 1-indexed
    }
  }
  
  return -1;
}

/**
 * 取得下一個可用 ID
 */
function getNextId_() {
  const sheet = getSheet_();
  const lastRow = sheet.getLastRow();
  
  if (lastRow <= 1) return 1;
  
  const ids = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  let maxId = 0;
  
  for (let i = 0; i < ids.length; i++) {
    const num = parseInt(ids[i][0]) || 0;
    if (num > maxId) maxId = num;
  }
  
  return maxId + 1;
}
