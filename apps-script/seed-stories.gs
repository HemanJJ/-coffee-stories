/**
 * 🌱 一次性匯入 10 篇咖啡故事到 Google Sheet
 * 
 * 使用方式：
 * 1. 將此函式貼到 Apps Script 的 Code.gs 最底部
 * 2. 上方選擇 seedStories → 點 ▶ 執行
 * 3. 執行完畢後，Google Sheet 會有 10 筆故事
 * 4. 可以把這個函式刪掉（只需要跑一次）
 */
function seedStories() {
  const stories = [
    {
      status: 'published', sort: 10, category: '愛', tag: 'Vol.01 愛',
      title: '留給你的半杯拿鐵',
      cover: 'https://images.unsplash.com/photo-1498804103079-a6351b050096?w=900&auto=format&fit=crop&q=82',
      excerpt: '他們沒有說過很多漂亮的話，只是每天清晨把第一口咖啡留給對方。後來她才明白，愛常常不是熱烈，是有人記得你的溫度。',
      type: 'video',
      mediaUrl: 'https://assets.mixkit.co/videos/preview/mixkit-coffee-is-poured-into-a-cup-32881-large.mp4',
      text: '她一直以為父親不太會愛人。\n\n母親走後，家裡安靜得像一只忘了上弦的鐘。父親每天早上仍煮兩杯咖啡，一杯黑咖啡給自己，一杯加很多奶，放在餐桌靠窗的位置。她看了幾次，終於忍不住說：「媽已經不在了。」\n\n父親沒有抬頭，只把那杯拿鐵往她面前推了推：「我知道。可是妳以前都偷喝她那杯。」\n\n那天她握著溫熱的杯子，忽然想起很多細節。雨天門口多出來的傘，便當盒裡被挑掉的蔥，深夜客廳那盞等她回家的燈。原來愛不一定會說出口，它有時只是半杯拿鐵，放在你剛好伸手碰得到的地方。\n\n咖啡喝到最後有一點苦，她卻第一次覺得，苦味也可以很甜。'
    },
    {
      status: 'published', sort: 20, category: '饒恕', tag: 'Vol.02 饒恕',
      title: '沒有寄出的道歉信',
      cover: 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=900&auto=format&fit=crop&q=82',
      excerpt: '他把道歉信放在抽屜最底層三年，直到某個下雨的下午，才發現饒恕不是讓過去沒發生，而是讓自己終於不用再住在那一天。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3',
      text: '信封泛黃的時候，他才承認自己其實一直在等一個機會。\n\n三年前，他和哥哥為了父親留下的小店吵到翻臉。最重的那句話是他說的：「你根本不配回這個家。」哥哥那天沒有回嘴，只把鑰匙放在櫃台上，轉身走進雨裡。\n\n後來他寫過一封道歉信，開頭改了十七次，結尾永遠停在「對不起」。他不敢寄，像是不寄出，錯就還沒有被正式承認。\n\n直到某天午後，一位老客人推門進來，說哥哥在隔壁城市開了間小咖啡攤，招牌上仍寫著父親的老字號。老客人喝著咖啡笑了笑：「他說，等你有空，可以過去坐坐。」\n\n他搭最晚一班車去。哥哥看見他，只問：「還喝以前那種嗎？」\n\n那一刻他才懂，饒恕不是把傷口說成沒痛過，而是有人願意在傷口旁邊，多放一張椅子。'
    },
    {
      status: 'published', sort: 30, category: '等候', tag: 'Vol.03 等候',
      title: '第七班公車',
      cover: 'https://images.unsplash.com/photo-1517457373958-b7bdd4587205?w=900&auto=format&fit=crop&q=82',
      excerpt: '她每天等同一班公車，不是因為那班最快，而是因為司機總會多停三秒。那些三秒，讓她重新相信世界還留著位置給慢一點的人。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3',
      text: '小芸的復健課在早上九點，她卻七點半就出門。\n\n車站離家只有五分鐘，但她走了二十分鐘。中風後的右腳不太聽話，每一步都像在和地面重新談判。前幾次，她總在公車關門前差一點趕上，司機看見她喘著氣，也只能抱歉地開走。\n\n直到第七班公車的司機開始等她。\n\n他沒有說什麼偉大的話，只是每天多停三秒。有時三秒剛好夠她走上第一階，有時不夠，他就再等三秒。車上的人偶爾皺眉，司機便說：「大家都會有走慢的一天。」\n\n半年後，小芸終於能穩穩走上車。她把一包耳掛咖啡放在投幣箱旁，小聲說謝謝。\n\n等候不是浪費時間。等候是有人相信，你正在用自己的速度回到生活裡。'
    },
    {
      status: 'published', sort: 40, category: '盼望', tag: 'Vol.04 盼望',
      title: '窗台上的小芽',
      cover: 'https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?w=900&auto=format&fit=crop&q=82',
      excerpt: '失業後的第三十天，他把咖啡渣埋進空盆。那株小芽沒有替他解決人生，卻每天用一點點綠意提醒他：不是所有沉默都叫結束。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3',
      text: '失業後的第三十天，他開始害怕手機震動。\n\n每一封沒有下文的履歷，都像一扇輕輕關上的門。他把鬧鐘關掉，窗簾拉上，連咖啡都只泡半杯，彷彿少喝一點，就能少感覺到自己還醒著。\n\n有天整理桌面，他看見母親寄來的訊息：「咖啡渣別丟，可以給土一點養分。」他笑了，覺得這句話荒唐又溫柔。家裡唯一的盆栽早就枯了，他還是把咖啡渣倒進去，澆了一點水。\n\n一週後，土裡冒出一點綠。\n\n那不是奇蹟，只是一株不知道從哪裡來的小芽。它很小，小到不能改變房租、面試和焦慮，可是每天早上，它都比昨天高一點點。\n\n他重新拉開窗簾，泡了一整杯咖啡。盼望有時不是遠方的大光，而是窗台上一點點綠，提醒你：生命還在往上。'
    },
    {
      status: 'published', sort: 50, category: '平安', tag: 'Vol.05 平安',
      title: '雨夜值班室',
      cover: 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=900&auto=format&fit=crop&q=82',
      excerpt: '急診室外的雨下了一整晚。她以為自己需要答案，後來才發現，在最慌的時候，有人陪你把一杯熱咖啡慢慢喝完，就是平安。',
      type: 'video',
      mediaUrl: 'https://assets.mixkit.co/videos/preview/mixkit-pouring-coffee-in-a-cup-seen-up-close-4450-large.mp4',
      text: '那晚雨很大，大到城市的聲音都被沖淡了。\n\n她坐在急診室外，手裡的號碼單被捏得皺成一團。父親在裡面檢查，醫師還沒出來。她一直滑手機，卻不知道自己在看什麼，只覺得每一分鐘都像被拉長。\n\n清潔阿姨推著車經過，停下來看了她一眼，從保溫袋拿出一杯咖啡：「我多買的，妳拿著。」\n\n她愣住，說不用。阿姨把咖啡放到她旁邊：「不用堅強，先喝熱的。」\n\n那杯咖啡其實很普通，便利商店的深焙，還有一點燙。但她用雙手捧著，忽然不再只聽見心跳聲。雨還在下，檢查還沒有結果，可是她的呼吸慢慢回來了。\n\n平安不是事情立刻變好。平安是風雨還在，你卻被一點溫度接住。'
    },
    {
      status: 'published', sort: 60, category: '恩典', tag: 'Vol.06 恩典',
      title: '多出來的一張早餐券',
      cover: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=900&auto=format&fit=crop&q=82',
      excerpt: '他只是把多出來的早餐券送給陌生人，沒想到多年後，那張券繞了一圈，變成某個早晨放在他桌上的熱咖啡。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3',
      text: '年輕時，他常去車站旁那間早餐店。\n\n有一次店員不小心多給他一張早餐券，他本來想退回去，卻看見門口有個學生翻著口袋，臉紅地問能不能晚點付。他走過去，把券遞給對方：「我今天剛好多一張。」\n\n那件事小到他很快就忘了。\n\n二十年後，他的公司倒了。中年人的失敗比較安靜，不會大哭大鬧，只是在早餐店點餐時，突然算起口袋裡還剩多少零錢。他坐在角落，假裝看報紙，心裡卻一片空。\n\n店員送來一份早餐和一杯咖啡，說：「有人替您付了。」\n\n櫃台旁站著一個西裝筆挺的男人，對他笑了笑：「以前在車站，有人也替我付過一頓早餐。」\n\n恩典常常不是從天上掉下來，它會借人的手，繞很遠的路，最後在你最需要的早晨，重新回到桌上。'
    },
    {
      status: 'published', sort: 70, category: '陪伴', tag: 'Vol.07 陪伴',
      title: '慢慢走的人',
      cover: 'https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=900&auto=format&fit=crop&q=82',
      excerpt: '外婆走得越來越慢，他也終於學會把行程排得越來越空。陪伴不是替對方走完路，而是願意把自己的速度借給他。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3',
      text: '外婆以前走路很快。\n\n她能一手提菜、一手牽他，穿過整個市場，還能準確記得哪攤番茄比較甜。後來外婆老了，走到巷口都要停三次。他一開始總忍不住看錶，提醒自己下一個會議還有多久。\n\n某個週日，他照例陪外婆去買咖啡豆。外婆在斑馬線前停下來，喘了一口氣，忽然說：「你如果忙，可以不用陪我。」\n\n他想說不忙，卻發現自己真的一直在急。\n\n那天他把手機關成靜音，陪外婆坐在路邊長椅。外婆說年輕時第一次喝咖啡，苦得皺眉，卻因為外公說香，她就學著喝。她說得很慢，他聽得也很慢。\n\n後來他才明白，陪伴不是把對方推到目的地，而是願意把自己的速度放低，和他一起經過那些再普通不過的街角。'
    },
    {
      status: 'published', sort: 80, category: '感恩', tag: 'Vol.08 感恩',
      title: '收據背面的謝謝',
      cover: 'https://images.unsplash.com/photo-1453614512568-c4024d13c247?w=900&auto=format&fit=crop&q=82',
      excerpt: '她每天買同一杯咖啡，直到離職那天才知道，自己隨手寫在收據背面的謝謝，曾經陪店員撐過很長一段低潮。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3',
      text: '她每天早上八點二十買一杯美式，不加糖。\n\n店員總是把杯蓋壓得很緊，提醒她小心燙。她也總是把收據翻到背面，寫一句「謝謝，今天也辛苦了」，再放進桌上的小盒子。她以為那只是自己的小習慣，像整理包包、擦掉杯口的水珠一樣微不足道。\n\n離職前一天，她最後一次走進咖啡店。店員認出她，從櫃台拿出一個信封，裡面是一疊收據。\n\n每張背面都有她的字。\n\n店員有些不好意思地說：「我剛來的時候常被客人罵，有幾次真的想辭職。可是每天看到妳寫那句話，就覺得也許我今天還可以撐一下。」\n\n她站在原地，忽然不知道該說什麼。\n\n感恩有時不是盛大的回報，只是一句真心的謝謝。你以為它輕得像紙，卻可能剛好成為某個人那天沒有放棄的重量。'
    },
    {
      status: 'published', sort: 90, category: '重新開始', tag: 'Vol.09 重新開始',
      title: '星期一的空白杯',
      cover: 'https://images.unsplash.com/photo-1521017432531-fbd92d768814?w=900&auto=format&fit=crop&q=82',
      excerpt: '她把辭職信寄出的那天，買了一只沒有圖案的白杯。不是因為她不害怕，而是因為空白終於不再像失去，而像可以重寫。',
      type: 'audio',
      mediaUrl: 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3',
      text: '她在同一家公司待了九年。\n\n九年足夠讓一個人熟悉影印機的脾氣、主管的語氣，以及自己每天把夢想往後挪一點的方式。她常說「等忙完這陣子」，可是這陣子一等就是九年。\n\n辭職信寄出的星期一，她沒有想像中的瀟灑。她在咖啡店坐了很久，手心一直冒汗，像是剛從一艘大船跳進水裡，還不知道岸在哪裡。\n\n店裡架上有一只白色馬克杯，沒有花紋，沒有標語。她買下來，請店員倒一杯熱拿鐵。\n\n杯子太白了，白得讓她有點害怕。可是喝到一半，她突然覺得，空白也許不是什麼都沒有，而是還沒有被寫壞。\n\n重新開始不是不怕，而是帶著害怕，仍然替明天留一只乾淨的杯子。'
    },
    {
      status: 'published', sort: 100, category: '回家', tag: 'Vol.10 回家',
      title: '巷口那盞燈',
      cover: 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=900&auto=format&fit=crop&q=82',
      excerpt: '他離家很久，以為回家需要一個完美理由。直到看見巷口那盞還亮著的燈，才知道有些地方不問你成敗，只問你餓不餓。',
      type: 'video',
      mediaUrl: 'https://assets.mixkit.co/videos/preview/mixkit-serving-a-cup-of-coffee-31518-large.mp4',
      text: '他已經三年沒有回家過年。\n\n每次母親打電話來，他都說工作忙。真正的原因其實很小，也很重：創業失敗後，他不知道該怎麼面對那些關心。親戚的問題、父親的沉默、母親故作輕鬆的語氣，都像一杯放冷的咖啡，苦得他不敢碰。\n\n除夕前一晚，他臨時買了車票。到家時已經十一點多，巷子裡的店都關了，只有家門口那盞黃燈還亮著。\n\n他站了很久，才按下門鈴。\n\n母親開門的第一句不是「你怎麼現在才回來」，也不是「事情處理好了嗎」。她只是把拖鞋推到他腳邊，說：「冰箱有滷肉，我去熱。你要不要先喝咖啡？」\n\n那一刻，他突然很想哭。\n\n回家原來不是證明自己過得很好。回家是有一個地方，知道你狼狽，仍然替你留燈、留飯，也留一個可以重新坐下的位置。'
    }
  ];

  // 逐筆呼叫 addStory 寫入
  stories.forEach(story => {
    addStory(story);
  });

  Logger.log('✅ 已匯入 ' + stories.length + ' 篇故事！');
}
