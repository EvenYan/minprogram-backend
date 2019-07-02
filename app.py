# coding=utf8
from flask import Flask, jsonify, request

app = Flask(__name__)

book_data = [{"_id":"1","rating":{"average":7.8,"numRaters":"11556"},"author":["吴晓波"],"pubdate":"2017-01-01","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E8%85%BE%E8%AE%AF%E4%BC%A0.jpg","title":"腾讯传","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"浙江大学出版社","summary":"腾讯官方唯一授权的权威传记\\r\\n著名财经作家吴晓波倾力之作  当市值最高的中国互联网公司，遇上中国财经界最冷静的一双眼睛  读懂腾讯，读懂中国互联网  .  内容简介  本书全景式地记录了腾讯崛起的经历，并以互联网的视角重新诠释了中国在融入全球化进程中的曲折与独特性。  从1998年开始创业到成为世界级互联网巨头，腾讯以即时通信工具起步，逐渐进入社交网络、互动娱乐、网络媒体、电子商务等领域，在超高速发展的同时亦饱受争议，在'3Q大战'的激烈冲突之后又进一步走向开放……腾讯的发展路径，亦是中国互联网企业成长的缩影。我们可以看到，中国的互联网人在应用性迭代和对本国消费者的行为了解上，找到了自己的办法，并开始领跑全球。  读懂腾讯，读懂中国互联网。","author_intro":"吴晓波：著名财经作家，'吴晓波频道'、蓝狮子出版创始人，常年从事中国企业史和公司案例研究。著有《大败局》I和II、《激荡三十年》《跌荡一百年》《浩荡两千年》《历代经济变革得失》等广具影响力的财经书籍，著作两次入选《亚洲周刊》年度最佳图书。"},
                 {"_id":"2","rating":{"average":9.3,"numRaters":"113143"},"author":["[美] 玛格丽特·米切尔"],"pubdate":"2000-09","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E9%A3%98.jpg","title":"飘","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"译林出版社","summary":"小说中的故事发生在1861年美国南北战争前夕。生活在南方的少女郝思嘉从小深受南方文化传统的熏陶，可在她的血液里却流淌着野性的叛逆因素。随着战火的蔓廷和生活环境的恶化，郝思嘉的叛逆个性越来越丰满，越鲜明，在一系列的的挫折中她改造了自我，改变了个人甚至整个家族的命运，成为时代时势造就的新女性的形象。  作品在描绘人物生活与爱情的同时，勾勒出南北双方在政治，经济，文化各个层次的异同，具有浓厚的史诗风格，堪称美国历史转折时期的真实写照，同时也成为历久不衰的爱情经典。","author_intro":"米切尔（Margaret Mitchell, 1900-1949）美国女作家。出生于美国南部佐治亚州亚特兰大市。父亲是个律师，曾任亚特兰大历史协会主席。米切尔曾就读于华盛顿神学院、马萨诸塞州的史密斯学院。其后，她曾担任地方报纸《亚特兰大报》的记者。1925年与约翰·马尔什结婚，婚后辞去报职，潜心写作。  米切尔一生中只发表了《飘》这部长篇巨著。她从1926年开始着力创作《飘》，10 年之后，作品问世，一出版就引起了强烈的反响。  由于家庭的熏陶，米切尔对美国历史，特别是南北战争时期美国南方的历史产生了浓厚的兴趣。她在家乡听闻了大量有关内战和战后重建时期的种种轶事和传闻，接触并阅读了大量有关内战的书籍。她自幼在南部城市亚特兰大成长，耳濡目染了美国南方的风土人情，这里的自然环境和社会环境成了米切尔文思纵横驰骋的背景和创作的源泉。"},
                 {"_id":"3","rating":{"average":9.1,"numRaters":"22088"},"author":["[美] 吴军"],"pubdate":"2011-08","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E6%B5%AA%E6%BD%AE%E4%B9%8B%E5%B7%85.jpg","title":"浪潮之巅","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"电子工业出版社","summary":"近一百多年来，总有一些公司很幸运地、有意识或无意识地站在技术革命的浪尖之上。在这十几年间，它们代表着科技的浪潮，直到下一波浪潮的来临。  从一百年前算起，AT\u0026T 公司、IBM 公司、苹果公司、英特尔公司、微软公司、思科公司、雅虎公司和Google公司都先后被幸运地推到了浪尖。虽然，它们来自不同的领域，中间有些已经衰落或正在衰落，但是它们都极度辉煌过。本书系统地介绍了这些公司成功的本质原因及科技工业一百多年的发展。  在极度商业化的今天，科技的进步和商机是分不开的。因此，本书也系统地介绍了影响到科技浪潮的风险投资公司，诸如 KPCB 和红杉资本，以及百年来为科技捧场的投资银行，例如高盛公司，等等。  在这些公司兴衰的背后，有着它必然的规律。本书不仅讲述科技工业的历史，更重在揭示它的规律性。","author_intro":"吴军博士，毕业于清华大学计算机系（本科）、电子工程系（硕士）和美国约翰 · 霍普金斯大学计算机科学系（博士）。在清华大学和约翰 · 霍普金斯大学期间，吴军博士致力于语音识别、自然语言处理，特别是统计语言模型的研究。他曾获得1995年全国人机语音智能接口会议的最佳论文奖和2000年Eurospeech的最佳论文奖。  吴军博士于2002年加入Google公司。在Google，他和Amit Singhal（Google院士，世界著名搜索专家）、Matt Cutts（Google反作弊官方发言人）等三位同事一起开创了网络搜索反作弊的研究领域，并因此获得Google工程奖。2003年，他和Google全球架构的总工程师朱会灿博士等共同成立了中日韩文搜索部门。吴军博士是当前Google中日韩文搜索算法的主要设计者。在Google其间，他还领导了许多研发项目，包括许多与中文相关的产品和自然语言处理的项目，并得到了当时公司首席执行官埃里克 · 施密特和创始人谢尔盖 · 布林的高度评价。此外，他还在谷歌黑板报上发表了《数学之美》系列博客。  吴军博士在国内外发表过数十篇论文，并获得和申请了十余项美国和国际专利。他于2005年起，当选为约翰 · 霍普金斯大学计算机系董事会董事。2007起担任风险投资基金中国世纪基金的董事。  2010年，吴军博士离开Google,加盟腾讯公司，担任负责搜索业务的副总裁。并担任国家重大专项“新一代搜索引擎和浏览器”项目的总负责人。"},
                 {"_id":"4","rating":{"average":8.5,"numRaters":"144714"},"author":["[英] 夏洛蒂·勃朗特"],"pubdate":"2003-11","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E7%AE%80%E7%88%B1%EF%BC%88%E8%8B%B1%E6%96%87%E5%85%A8%E6%9C%AC%EF%BC%89.jpg","title":"简爱（英文全本）","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"世界图书出版公司","summary":"《简爱》是英国女作家夏洛蒂·勃朗特的代表作品。女主人公简爱是一个追赶求平等与自主的知识女性形象，小说以其感人的对于一位“灰姑娘式”人物奋斗史的刻划取胜，《简爱》也是女性文学的代表作品。","author_intro":"暂无"},
                 {"_id":"5","rating":{"average":8.8,"numRaters":"132280"},"author":["[英] 简·奥斯汀"],"pubdate":"1993-07","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E5%82%B2%E6%85%A2%E4%B8%8E%E5%81%8F%E8%A7%81.jpg","title":"傲慢与偏见","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"人民文学出版社","summary":"《傲慢与偏见》是简·奥斯汀的代表作，是一部描写爱情与婚姻的经典小说。作品以男女主人公达西和伊丽莎白由于傲慢和偏见而产生的爱情纠葛为线索，共写了四起姻缘：伊丽莎白与达西、简与宾利、莉迪亚与威克姆、夏洛蒂与柯林斯。伊丽莎白、简和莉迪亚是贝内特家五个女儿中的三个姐妹，而夏洛蒂则是她们的邻居，也是伊丽莎白的朋友。男主人公达西与宾利是好友，且与威克姆一起长大，而柯林斯则是贝内特家的远房亲戚。  贝内特夫妇五个女儿待字闺中，没有子嗣，依照当时法律，他们死后家产须由远房内侄柯林斯继承，因此把五个女儿嫁到有钱人家，成了贝内特太太最大的心愿。宾利，一位未婚富家子弟，租赁了贝内特家附近的内瑟菲尔德庄园，成为众人注目的焦点和谈论的话题。不久，宾利就与美丽贤淑的大小姐简相爱了。宾利的朋友达西对聪明直率的二小姐伊丽莎白颇有好感，却因在一次舞会上出言不逊使伊丽莎白对他心存偏见。品行不端的威克姆告诉伊丽莎白，他是达西庄园已故总管的儿子，与达西一起长大，达西的父亲先前许诺给他的教职，被达西无端剥夺了。而达西则因为伊丽莎白的母亲及其他妹妹的缘故，劝说宾利中止与简的关系，结果四人不欢而散。威克姆对达西的诋毁，以及达西的劝说对简造成的伤害进一步加深了伊丽莎白对达西的偏见。  柯林斯为心安理得地继承财产，决定从贝内特家五个漂亮的女儿之中挑选一个“妻子”，于是向伊丽莎白求婚。遭到拒绝后，他马上转向尚未婚配急于找到“归宿”的夏洛蒂小姐，竟然得到应允。伊丽莎白应邀到新婚的柯林斯和夏洛蒂夫妇家中做客，不期遇见前来探望凯瑟琳夫人的达西。达西为伊丽莎白所倾倒，向她求婚，但因其言辞的傲慢，遭到伊丽莎白的愤然拒绝。同时，伊丽莎白指责达西对威克姆冷酷无情，更不应该破坏宾利同简的爱情。事后达西写信为自己申辩，令伊丽莎白的偏见逐渐消除。  伊丽莎白随舅父舅妈出游时经过达西的庄园，以为达西不在，进去参观，不料达西突然归来，伊丽莎白感到十分窘迫。然而，达西丝毫没有以往的傲慢，非常热情地接待了他们。此时，伊丽莎白突然接到家信，得知威克姆带着妹妹莉迪亚私奔了！匆忙回家后，全家一筹莫展，不料达西暗访到两人的行踪，出资促成他们的婚事并安排了他们的生活，为贝内特一家保全了尊严。此事使伊丽莎白与达西尽释前嫌，宾利也和简重修旧好，最后有情人终成眷属。","author_intro":"简·奥斯汀（Jane Austen，1775年12月16日－1817年7月18日）是英国著名女性小说家，她的作品主要关注乡绅家庭女性的婚姻和生活，以女性特有的细致入微的观察力和活泼风趣的文字真实地描绘了她周围世界的小天地。  奥斯汀终身未婚，家道小康。由于居住在乡村小镇，接触到的是中小地主、牧师等人物以及他们恬静、舒适的生活环境，因此她的作品里没有重大的社会矛盾。她以女性特有的细致入微的观察力，真实地描绘了她周围世界的小天地，尤其是绅士淑女间的婚姻和爱情风波。她的作品格调轻松诙谐，富有喜剧性冲突，深受读者欢迎。从18世纪末到19世纪初，庸俗无聊的“感伤小说”和“哥特小说”充斥英国文坛，而奥斯汀的小说破旧立新，一反常规地展现了当时尚未受到资本主义工业革命冲击的英国乡村中产阶级的日常生活和田园风光。她的作品往往通过喜剧性的场面嘲讽人们的愚蠢、自私、势利和盲目自信等可鄙可笑的弱点。奥斯汀的小说出现在19世纪初叶，一扫风行一时的假浪漫主义潮流，继承和发展了英国18世纪优秀的现实主义传统，为19世纪现实主义小说的高潮做了准备。虽然其作品反映的广度和深度有限，但她的作品如“两寸牙雕”，从一个小窗口中窥视到整个社会形态和人情世故，对改变当时小说创作中的庸俗风气起了好的作用，在英国小说的发展史上有承上启下的意义，被誉为地位“可与莎士比亚平起平坐”的作家。  简·奥斯丁出生在英国汉普郡斯蒂文顿镇的一个牧师家庭，过着祥和、小康的乡居生活。兄弟姐妹共八人，奥斯丁排行第六。她从未进过正规学校，只是九岁时，曾被送往姐姐的学校伴读。她的姐姐卡桑德拉是她毕生最好的朋友，然而奥斯丁的启蒙教育却更多得之于她的父亲。奥斯丁酷爱读书写作，还在十一、二岁的时候，便已开始以写作为乐事了。成年后奥斯丁随全家迁居多次。1817年，奥斯丁已抱病在身，为了求医方便，最后一次举家再迁。然而在到了曼彻斯特后不过两个多月，她便去世了。死后安葬在温彻斯特大教堂。简·奥斯丁终身未嫁。逝世时仅为四十一岁。"},
                 {"_id":"6","rating":{"average":8.3,"numRaters":"65510"},"author":["[法] 雨果"],"pubdate":"1982-06","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E5%B7%B4%E9%BB%8E%E5%9C%A3%E6%AF%8D%E9%99%A2.jpg","title":"巴黎圣母院","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"人民文学出版社","summary":"《巴黎圣母院》是法国文豪维克多·雨果第一部引起轰动效应的浪漫派小说。小说以十五世纪路易十一统治下的法国为背景，通过一个纯洁无辜的波希米亚女郎惨遭迫害的故事，揭露了教士的阴险卑鄙，宗教法庭的野蛮残忍，贵族的荒淫无耻和国王的专横残暴。作品鲜明地体现了反封建、反教会的意识和对人民群众的赞颂。","author_intro":"维克多·马里·雨果是一名法国浪漫主义作家。他是法国浪漫主义文学的的代表人物和19世纪前期积极浪漫主义文学运动的领袖，法国文学史上卓越的作家。雨果几乎经历了19世纪法国的所有重大事变。一生创作了众多诗歌、小说、剧本、各种散文和文艺评论及政论文章。代表作有《巴黎圣母院》、《九三年》、和《悲惨世界》等。"},
                 {"_id":"7","rating":{"average":8.4,"numRaters":"501"},"author":["[美] 大卫· 哈维 "],"pubdate":"2009-12","image":"https://book-pic-1255596198.cos.ap-guangzhou.myqcloud.com/%E5%B7%B4%E9%BB%8E%E5%9F%8E%E8%AE%B0.jpg","title":"巴黎城记","_openid":"oRB0d5J55kfHTyciaFR8cp5eOwhk","publisher":"广西师范大学出版社","summary":"巴黎一直是世界上最有影响力的城市，但它却是在“第二帝国”时期才摇身成为我们今日所知的现代性样板。在1848到1871年两次失败的革命之间，巴黎经历了一场惊人的转变，俗称“巴黎大改造”。奥斯曼男爵，传奇的巴黎首长，一手打造巴黎的外观，以今日巴黎四处可见的林荫大道，取代了昔日的中世纪城市面貌，成就了今日如梦如幻的巴黎。这段时期也兴起了以高度发达的金融业为主体的新资本主义形式，以及现代的大众消费文化。城市外貌及社会景观的剧变，带来崭新的现代主义文化，同时也导致巴黎沿着阶级的界线断裂，结果是1871年巴黎公社的建立，以及随后的血腥镇压。哈维的全景式观照与戏剧式的叙述，使得阅读本书一直充满着张力。本书堪与卡尔•休斯克《世纪末的维也纳》媲美，是研究现代都市兴起的历史杰作。  推荐——  当你阅读奥斯曼的、巴尔扎克的，以及哈维的巴黎的时候，你可能会忽然意识到自己身边发生的类似情景。或许，你自己的城市，也曾经有过，或正在经受着：痛苦的“创造性破坏”的过程。  ——唐晓峰，北京大学城市与环境学院历史地理研究所教授  本雅明用意象蒙太奇重构了“巴黎，十九世纪的首都”，让我们置身于闲逛者、“波希米亚人”、拾荒者、妓女之中，行走在拱廊、林荫大道乃至街垒之间。大卫·哈维给出的是更冷峻的分析和论证：“巴黎，现代性之都”与其说是现代人间天城蓝图的实现，不如说是帝国和资本的联手杰作。从本雅明到哈维，我们看到了西方左翼的巴黎研究从文化批评到政治经济分析的深化。  ──刘北成，清华大学历史系教授  哈维的巴黎是对本雅明的巴黎的补充，而不是一种对抗。本雅明的巴黎，看上去像是美学；而哈维的巴黎，是政治经济学。本雅明的拱廊计划无法效仿，而哈维的研究可以说是历史地理学的完美一课。本雅明是难以望其项背的天才，哈维则是一个能让众人学习的典范。  ——汪民安，北京外国语大学外国文学研究所教授  持续十七年的巴黎大改造，将贫苦的老巴黎人驱赶至郊区，换来一个光鲜的“现代性之都”，随后巴黎公社革命爆发，二者有何内在联系？当贫困在郊区被“世袭”下来，2005年巴黎北郊的穷孩子走上街头焚烧富人的汽车，2007年郊区青年再次暴动，甚至端起了猎枪——“巴黎骚乱”，这场现代巴黎的“样板戏”一次次上演的时候，我脑海里浮现的，还是那次大改造的影子。一百多年前，让老巴黎天翻地覆的铁铲，所制造的贫富分区等“遗产”，对今日之城市动荡，负有怎样的责任？我想在这本书中找到的答案。  ——王军，新华社高级记者，著有《城记》《采访本上的城市》","author_intro":"大卫·哈维（David Harvey），1935年生于英国肯特郡，1957年获英国剑桥大学学士学位，1961年获该校博士学位。曾任教于英国布里斯托尔大学、美国宾州大学、英国牛津大学和美国约翰·霍普金斯大学，现任教于纽约市立大学研究生中心和伦敦经济学院。哈维是当今世界最主要的批判性知识分子，是当代西方新马克思主义的重要代表人物之一。他至今已经出版了十部著作，其中包括《地理学中的解释》、《社会正义与城市》、《资本的限度》、《资本的都市化》、《后现代的状况》，以及《资本的空间》和《新帝国主义》等。  译者简介  黄煜文，1974年生，台湾大学历史学硕士，现为专职译者，译著甚丰。重要译作有《论历史》、《世纪末的维也纳》、《肉体与石头》、《孩子的历史》、《错的是我们，不是我：家暴的动力关系》、《惩罚与现代社会》、《你的权利从哪里来？》等。"},
                ]


@app.route("/")
def index():
    return jsonify(book_data)
    

@app.route("/book/<int:id>")
def detail(id):
    if isinstance(id, int) and id <= len(book_data):
        return jsonify(book_data[id-1])
    return "图书ID不合法"



@app.route("/search/")
def search_book():
    q = request.args.get("q")
    if not q:
        return "请输入查询参数"
    result_book = []
    for i in book_data:
        if q in i.get("title"):
            result_book.append(i)
    if not result_book:
        return ""
    return jsonify(result_book)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
