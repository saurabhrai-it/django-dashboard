import ast

user = '[[1551769490000,27],[1551769502000,27],[1551769513000,31],[1551769524000,35],[1551769536000,39],[1551769547000,46],[1551769558000,51],[1551769569000,55],[1551769581000,60],[1551769592000,69],[1551769603000,72],[1551769615000,82],[1551769626000,85],[1551769637000,89],[1551769649000,92],[1551769660000,94],[1551769671000,105],[1551769682000,109],[1551769694000,118],[1551769705000,123],[1551769716000,126],[1551769728000,131],[1551769739000,138],[1551769750000,143],[1551769762000,147],[1551769773000,150],[1551769784000,153],[1551769795000,170],[1551769807000,179],[1551769818000,182],[1551769829000,185],[1551769841000,189],[1551769852000,195],[1551769863000,202],[1551769875000,205],[1551769886000,211],[1551769897000,218],[1551769908000,224],[1551769920000,229],[1551769931000,237],[1551769942000,241],[1551769954000,243],[1551769965000,246],[1551769976000,253],[1551769988000,260],[1551769999000,269],[1551770010000,274],[1551770021000,277],[1551770033000,282],[1551770044000,287],[1551770055000,294],[1551770067000,299],[1551770078000,300],[1551770089000,305],[1551770101000,314],[1551770112000,328],[1551770123000,334],[1551770135000,336],[1551770146000,341],[1551770157000,345],[1551770168000,351],[1551770180000,357],[1551770191000,362],[1551770202000,370],[1551770214000,375],[1551770225000,377],[1551770236000,388],[1551770248000,392],[1551770259000,393],[1551770270000,399],[1551770281000,402],[1551770293000,410],[1551770304000,420],[1551770315000,423],[1551770327000,430],[1551770338000,432],[1551770349000,436],[1551770361000,445],[1551770372000,450],[1551770383000,452],[1551770394000,456],[1551770406000,463],[1551770417000,474],[1551770428000,485],[1551770440000,486],[1551770451000,493],[1551770462000,496],[1551770474000,501],[1551770485000,508],[1551770496000,511],[1551770507000,522],[1551770519000,525],[1551770530000,528],[1551770541000,538],[1551770553000,543],[1551770564000,545],[1551770575000,549],[1551770587000,553],[1551770598000,559],[1551770609000,571],[1551770620000,574],[1551770632000,581],[1551770643000,583],[1551770654000,586],[1551770666000,594],[1551770677000,599],[1551770688000,605],[1551770700000,606],[1551770711000,613],[1551770722000,623],[1551770733000,631],[1551770745000,639],[1551770756000,642],[1551770767000,647],[1551770779000,650],[1551770790000,658],[1551770801000,662],[1551770813000,673],[1551770824000,676],[1551770835000,679],[1551770846000,686],[1551770858000,693],[1551770869000,698],[1551770880000,699],[1551770892000,704],[1551770903000,709],[1551770914000,720],[1551770926000,726],[1551770937000,730],[1551770948000,734],[1551770959000,738],[1551770971000,743],[1551770982000,750],[1551770993000,756],[1551771005000,757],[1551771016000,764],[1551771027000,772],[1551771039000,779],[1551771050000,789],[1551771061000,792],[1551771072000,798],[1551771084000,802],[1551771095000,806],[1551771106000,814],[1551771118000,822],[1551771129000,827],[1551771140000,831],[1551771152000,834],[1551771163000,844],[1551771174000,849],[1551771185000,850],[1551771197000,854],[1551771208000,860],[1551771219000,867],[1551771231000,879],[1551771242000,880],[1551771253000,886],[1551771265000,889],[1551771276000,891],[1551771287000,901],[1551771299000,906],[1551771310000,909],[1551771321000,915],[1551771332000,922],[1551771344000,929],[1551771355000,936],[1551771366000,943],[1551771378000,949],[1551771389000,953],[1551771400000,954],[1551771412000,965],[1551771423000,972],[1551771434000,979],[1551771445000,982],[1551771457000,984],[1551771468000,994],[1551771479000,999],[1551771491000,1002],[1551771502000,1005],[1551771513000,1010],[1551771525000,1017],[1551771536000,1029],[1551771547000,1031],[1551771558000,1037],[1551771570000,1041],[1551771581000,1042],[1551771592000,1050],[1551771604000,1057],[1551771615000,1060],[1551771626000,1066],[1551771638000,1071],[1551771649000,1079],[1551771660000,1086],[1551771671000,1090],[1551771683000,1100],[1551771694000,1104],[1551771705000,1107],[1551771717000,1113],[1551771728000,1122],[1551771739000,1130],[1551771751000,1134],[1551771762000,1135],[1551771773000,1141],[1551771784000,1150],[1551771796000,1153],[1551771807000,1157],[1551771818000,1160],[1551771830000,1169],[1551771841000,1176],[1551771852000,1182],[1551771864000,1188],[1551771875000,1191],[1551771886000,1194],[1551771897000,1197],[1551771909000,1208],[1551771920000,1212],[1551771931000,1217],[1551771943000,1223],[1551771954000,1230],[1551771965000,1234],[1551771977000,1241],[1551771988000,1247],[1551771999000,1254],[1551772010000,1260],[1551772022000,1261],[1551772033000,1272],[1551772044000,1282],[1551772056000,1284],[1551772067000,1288],[1551772078000,1290],[1551772090000,1299],[1551772101000,1305],[1551772112000,1308],[1551772123000,1311],[1551772135000,1319],[1551772146000,1325],[1551772157000,1334],[1551772169000,1339],[1551772180000,1341],[1551772191000,1347],[1551772203000,1348],[1551772214000,1357],[1551772225000,1363],[1551772236000,1367],[1551772248000,1375],[1551772259000,1379],[1551772270000,1384],[1551772282000,1392],[1551772293000,1395],[1551772304000,1404],[1551772316000,1410],[1551772327000,1412],[1551772338000,1420],[1551772350000,1433],[1551772361000,1435],[1551772372000,1440],[1551772383000,1441],[1551772395000,1448],[1551772406000,1456],[1551772417000,1458],[1551772429000,1463],[1551772440000,1468],[1551772451000,1476],[1551772463000,1484],[1551772474000,1488],[1551772485000,1494],[1551772496000,1497],[1551772508000,1499],[1551772519000,1504],[1551772530000,1515],[1551772542000,1518],[1551772553000,1527],[1551772564000,1529],[1551772576000,1534],[1551772587000,1542],[1551772598000,1545],[1551772609000,1552],[1551772621000,1560],[1551772632000,1563],[1551772643000,1569],[1551772655000,1583],[1551772666000,1587],[1551772677000,1590],[1551772689000,1592],[1551772700000,1598],[1551772711000,1606],[1551772722000,1610],[1551772734000,1614],[1551772745000,1619],[1551772756000,1627],[1551772768000,1632],[1551772779000,1638],[1551772790000,1647],[1551772802000,1647],[1551772813000,1651],[1551772824000,1654],[1551772835000,1663],[1551772847000,1670],[1551772858000,1677],[1551772869000,1680],[1551772881000,1686],[1551772892000,1690],[1551772903000,1697],[1551772915000,1702],[1551772926000,1708],[1551772937000,1715],[1551772948000,1719],[1551772960000,1731],[1551772971000,1740],[1551772982000,1740],[1551772994000,1744],[1551773005000,1749],[1551773016000,1753],[1551773028000,1762],[1551773039000,1764],[1551773050000,1769],[1551773061000,1779],[1551773073000,1782],[1551773084000,1789],[1551773095000,1796],[1551773107000,1799],[1551773118000,1802],[1551773129000,1805],[1551773141000,1811],[1551773152000,1821],[1551773163000,1828],[1551773174000,1831],[1551773186000,1837],[1551773197000,1839],[1551773208000,1848],[1551773220000,1851],[1551773231000,1857],[1551773242000,1864],[1551773254000,1869],[1551773265000,1881],[1551773276000,1890],[1551773287000,1892],[1551773299000,1895],[1551773310000,1899],[1551773321000,1903],[1551773333000,1913],[1551773344000,1915],[1551773355000,1919],[1551773367000,1931],[1551773378000,1932],[1551773389000,1939],[1551773400000,1946],[1551773412000,1950],[1551773423000,1954],[1551773434000,1956],[1551773446000,1961],[1551773457000,1970],[1551773468000,1979],[1551773480000,1983],[1551773491000,1988],[1551773502000,1990],[1551773514000,1997],[1551773525000,2002],[1551773536000,2008],[1551773547000,2012],[1551773559000,2018],[1551773570000,2031],[1551773581000,2039],[1551773593000,2044],[1551773604000,2047],[1551773615000,2049],[1551773627000,2056],[1551773638000,2060],[1551773649000,2066],[1551773660000,2070],[1551773672000,2081],[1551773683000,2084],[1551773694000,2088],[1551773706000,2096],[1551773717000,2102],[1551773728000,2105],[1551773740000,2106],[1551773751000,2113],[1551773762000,2118],[1551773773000,2130],[1551773785000,2134],[1551773796000,2137],[1551773807000,2143],[1551773819000,2145],[1551773830000,2154],[1551773841000,2159],[1551773853000,2163],[1551773864000,2167],[1551773875000,2180],[1551773886000,2187],[1551773898000,2195],[1551773909000,2198],[1551773920000,2199],[1551773932000,2207],[1551773943000,2209],[1551773954000,2218],[1551773966000,2221],[1551773977000,2231],[1551773988000,2236],[1551773999000,2238],[1551774011000,2244],[1551774022000,2253],[1551774033000,2256],[1551774045000,2259],[1551774056000,2262],[1551774067000,2267],[1551774079000,2281],[1551774090000,2286],[1551774101000,2287],[1551774112000,2295],[1551774124000,2296],[1551774135000,2302],[1551774146000,2309],[1551774158000,2313],[1551774169000,2318],[1551774180000,2327],[1551774192000,2336],[1551774203000,2347],[1551774214000,2349],[1551774225000,2352],[1551774237000,2356],[1551774248000,2360],[1551774259000,2367],[1551774271000,2373],[1551774282000,2381],[1551774293000,2388],[1551774305000,2389],[1551774316000,2393],[1551774327000,2404],[1551774338000,2406],[1551774350000,2411],[1551774361000,2412],[1551774372000,2418],[1551774384000,2430],[1551774395000,2436],[1551774406000,2439],[1551774418000,2444],[1551774429000,2447],[1551774440000,2451],[1551774451000,2460],[1551774463000,2465],[1551774474000,2469],[1551774485000,2475],[1551774497000,2485],[1551774508000,2496],[1551774519000,2499],[1551774531000,2505],[1551774542000,2506],[1551774553000,2512],[1551774564000,2515],[1551774576000,2523],[1551774587000,2532],[1551774598000,2538],[1551774610000,2541],[1551774621000,2544],[1551774632000,2552],[1551774644000,2558],[1551774655000,2562],[1551774666000,2563],[1551774678000,2568],[1551774689000,2578],[1551774700000,2586],[1551774711000,2592],[1551774723000,2595],[1551774734000,2599],[1551774745000,2602],[1551774757000,2608],[1551774768000,2617],[1551774779000,2619],[1551774791000,2626],[1551774802000,2632],[1551774813000,2643],[1551774824000,2651],[1551774836000,2655],[1551774847000,2657],[1551774858000,2663],[1551774870000,2666],[1551774881000,2672],[1551774892000,2683],[1551774904000,2689],[1551774915000,2692],[1551774926000,2695],[1551774937000,2698],[1551774949000,2711],[1551774960000,2712],[1551774971000,2715],[1551774983000,2720],[1551774994000,2727],[1551775005000,2737],[1551775017000,2742],[1551775028000,2745],[1551775039000,2750],[1551775050000,2754],[1551775062000,2757],[1551775073000,2767],[1551775084000,2770],[1551775096000,2777],[1551775107000,2783],[1551775118000,2788],[1551775130000,2802],[1551775141000,2805],[1551775152000,2808],[1551775163000,2814],[1551775175000,2817],[1551775186000,2822],[1551775197000,2832],[1551775209000,2840],[1551775220000,2844],[1551775231000,2847],[1551775243000,2848],[1551775254000,2860],[1551775265000,2863],[1551775276000,2866],[1551775288000,2870],[1551775299000,2877],[1551775310000,2887],[1551775322000,2892],[1551775333000,2896],[1551775344000,2902],[1551775356000,2904],[1551775367000,2908],[1551775378000,2915],[1551775389000,2921],[1551775401000,2928],[1551775412000,2934],[1551775423000,2937],[1551775435000,2949],[1551775446000,2956],[1551775457000,2960],[1551775469000,2964],[1551775480000,2967],[1551775491000,2973],[1551775502000,2981],[1551775514000,2991],[1551775525000,2995],[1551775536000,2997],[1551775548000,3001],[1551775559000,3007],[1551775570000,3015],[1551775582000,3018],[1551775593000,3021],[1551775604000,3028],[1551775615000,3036],[1551775627000,3043],[1551775638000,3047],[1551775649000,3053],[1551775661000,3055],[1551775672000,3060],[1551775683000,3063],[1551775695000,3073],[1551775706000,3079],[1551775717000,3084],[1551775728000,3089],[1551775740000,3093],[1551775751000,3108],[1551775762000,3111],[1551775774000,3114],[1551775785000,3120],[1551775796000,3123],[1551775808000,3129],[1551775819000,3141],[1551775830000,3147],[1551775842000,3148],[1551775853000,3153],[1551775864000,3155],[1551775875000,3166],[1551775887000,3170],[1551775898000,3171],[1551775909000,3180],[1551775921000,3186],[1551775932000,3192],[1551775943000,3199],[1551775955000,3202],[1551775966000,3207],[1551775977000,3210],[1551775988000,3212],[1551776000000,3223],[1551776011000,3230],[1551776022000,3235],[1551776034000,3240],[1551776045000,3244],[1551776056000,3252],[1551776068000,3263],[1551776079000,3264],[1551776090000,3273],[1551776101000,3273],[1551776113000,3279],[1551776124000,3292],[1551776135000,3297],[1551776147000,3300],[1551776158000,3303],[1551776169000,3306],[1551776181000,3315],[1551776192000,3321],[1551776203000,3323],[1551776214000,3329],[1551776226000,3337],[1551776237000,3341],[1551776248000,3350],[1551776260000,3352],[1551776271000,3360],[1551776282000,3360],[1551776294000,3364],[1551776305000,3372],[1551776316000,3379],[1551776327000,3388],[1551776339000,3390],[1551776350000,3395],[1551776361000,3399],[1551776373000,3411],[1551776384000,3416],[1551776395000,3422],[1551776407000,3424],[1551776418000,3429],[1551776429000,3441],[1551776440000,3447],[1551776452000,3453],[1551776463000,3454],[1551776474000,3456],[1551776486000,3458],[1551776497000,3465],[1551776508000,3465],[1551776520000,3466],[1551776531000,3474],[1551776542000,3474],[1551776553000,3477],[1551776565000,3480],[1551776576000,3483],[1551776587000,3483],[1551776599000,3483],[1551776610000,3484],[1551776621000,3492],[1551776633000,3492],[1551776644000,3492],[1551776655000,3492],[1551776666000,3492],[1551776678000,3492],[1551776689000,3492],[1551776700000,3492],[1551776712000,3492],[1551776723000,3492],[1551776734000,3492],[1551776746000,3492],[1551776757000,3492],[1551776768000,3492],[1551776779000,3492],[1551776791000,3492],[1551776802000,3492],[1551776813000,3492],[1551776825000,3492],[1551776836000,3492],[1551776847000,3492],[1551776859000,3492],[1551776870000,3492],[1551776881000,3492],[1551776893000,3492],[1551776904000,3492],[1551776915000,3492],[1551776926000,3492],[1551776938000,3492],[1551776949000,3492],[1551776960000,3492],[1551776972000,3492],[1551776983000,3492],[1551776994000,3492],[1551777006000,3492],[1551777017000,3492],[1551777028000,3492],[1551777039000,3492],[1551777051000,3492],[1551777062000,3492],[1551777073000,3492],[1551777085000,3492],[1551777096000,3492],[1551777107000,3492],[1551777119000,3492],[1551777130000,3492],[1551777141000,3492],[1551777152000,3492],[1551777164000,3492],[1551777175000,3492],[1551777186000,3492],[1551777198000,3492],[1551777209000,3492],[1551777220000,3492],[1551777232000,3492],[1551777243000,3492],[1551777254000,3492],[1551777265000,3492],[1551777277000,3492],[1551777288000,3492],[1551777299000,3492],[1551777311000,3492],[1551777322000,3492],[1551777333000,3492],[1551777345000,3492],[1551777356000,3492],[1551777367000,3492],[1551777378000,3492],[1551777390000,3492],[1551777401000,3492],[1551777412000,3492],[1551777424000,3492],[1551777435000,3492],[1551777446000,3492],[1551777458000,3492],[1551777469000,3492],[1551777480000,3492],[1551777491000,3492],[1551777503000,3492],[1551777514000,3492],[1551777525000,3492],[1551777537000,3492],[1551777548000,3492],[1551777559000,3492],[1551777571000,3492],[1551777582000,3492],[1551777593000,3492],[1551777604000,3492],[1551777616000,3492],[1551777627000,3492],[1551777638000,3492],[1551777650000,3492],[1551777661000,3492],[1551777672000,3492],[1551777684000,3492],[1551777695000,3492],[1551777706000,3492],[1551777717000,3492],[1551777729000,3492],[1551777740000,3492],[1551777751000,3492],[1551777763000,3492],[1551777774000,3492],[1551777785000,3492],[1551777797000,3492],[1551777808000,3492],[1551777819000,3492],[1551777830000,3492],[1551777842000,3492],[1551777853000,3492],[1551777864000,3492],[1551777876000,3492],[1551777887000,3492],[1551777898000,3492],[1551777910000,3492],[1551777921000,3492],[1551777932000,3492],[1551777943000,3492],[1551777955000,3492],[1551777966000,3492],[1551777977000,3492],[1551777989000,3492],[1551778000000,3492],[1551778011000,3492],[1551778023000,3492],[1551778034000,3492],[1551778045000,3492],[1551778057000,3492],[1551778068000,3492],[1551778079000,3492],[1551778090000,3492],[1551778102000,3492],[1551778113000,3492],[1551778124000,3492],[1551778136000,3492],[1551778147000,3492],[1551778158000,3492],[1551778170000,3492],[1551778181000,3492],[1551778192000,3492],[1551778203000,3492],[1551778215000,3492],[1551778226000,3492],[1551778237000,3492],[1551778249000,3492],[1551778260000,3492],[1551778271000,3492],[1551778283000,3492],[1551778294000,3492],[1551778305000,3492],[1551778316000,3492],[1551778328000,3492],[1551778339000,3492],[1551778350000,3492],[1551778362000,3492],[1551778373000,3492],[1551778384000,3492],[1551778396000,3492],[1551778407000,3492],[1551778418000,3492],[1551778429000,3492],[1551778441000,3492],[1551778452000,3492],[1551778463000,3492],[1551778475000,3492],[1551778486000,3492],[1551778497000,3492],[1551778509000,3492],[1551778520000,3492],[1551778531000,3492],[1551778542000,3492],[1551778554000,3492],[1551778565000,3492],[1551778576000,3492],[1551778588000,3492],[1551778599000,3492],[1551778610000,3492],[1551778622000,3492],[1551778633000,3492],[1551778644000,3492],[1551778655000,3492],[1551778667000,3492],[1551778678000,3492],[1551778689000,3492],[1551778701000,3492],[1551778712000,3492],[1551778723000,3492],[1551778735000,3492],[1551778746000,3492],[1551778757000,3492],[1551778768000,3492],[1551778780000,3492],[1551778791000,3492],[1551778802000,3492],[1551778814000,3492],[1551778825000,3492],[1551778836000,3492],[1551778848000,3492],[1551778859000,3492],[1551778870000,3492],[1551778881000,3492],[1551778893000,3492],[1551778904000,3492],[1551778915000,3492],[1551778927000,3492],[1551778938000,3492],[1551778949000,3492],[1551778961000,3492],[1551778972000,3492],[1551778983000,3492],[1551778994000,3492],[1551779006000,3492],[1551779017000,3492],[1551779028000,3492],[1551779040000,3492],[1551779051000,3492],[1551779062000,3492],[1551779074000,3492],[1551779085000,3492],[1551779096000,3492],[1551779107000,3492],[1551779119000,3492],[1551779130000,3492],[1551779141000,3492],[1551779153000,3492],[1551779164000,3492],[1551779175000,3492],[1551779187000,3492],[1551779198000,3492],[1551779209000,3492],[1551779221000,3492],[1551779232000,3492],[1551779243000,3492],[1551779254000,3492],[1551779266000,3492],[1551779277000,3492],[1551779288000,3492],[1551779300000,3492],[1551779311000,3492],[1551779322000,3492],[1551779334000,3492],[1551779345000,3492],[1551779356000,3492],[1551779367000,3492],[1551779379000,3492],[1551779390000,3492],[1551779401000,3492],[1551779413000,3492],[1551779424000,3492],[1551779435000,3492],[1551779447000,3492],[1551779458000,3492],[1551779469000,3492],[1551779480000,3492],[1551779492000,3492],[1551779503000,3492],[1551779514000,3492],[1551779526000,3492],[1551779537000,3492],[1551779548000,3492],[1551779560000,3492],[1551779571000,3492],[1551779582000,3492],[1551779593000,3492],[1551779605000,3492],[1551779616000,3492],[1551779627000,3492],[1551779639000,3492],[1551779650000,3492],[1551779661000,3492],[1551779673000,3492],[1551779684000,3492],[1551779695000,3492],[1551779706000,3492],[1551779718000,3492],[1551779729000,3492],[1551779740000,3492],[1551779752000,3492],[1551779763000,3492],[1551779774000,3492],[1551779786000,3492],[1551779797000,3492],[1551779808000,3492],[1551779819000,3492],[1551779831000,3492],[1551779842000,3492],[1551779853000,3492],[1551779865000,3492],[1551779876000,3492],[1551779887000,3492],[1551779899000,3492],[1551779910000,3492],[1551779921000,3492],[1551779932000,3492],[1551779944000,3492],[1551779955000,3492],[1551779966000,3492],[1551779978000,3492],[1551779989000,3492],[1551780000000,3492],[1551780012000,3492],[1551780023000,3492],[1551780034000,3492],[1551780045000,3492],[1551780057000,3492],[1551780068000,3492],[1551780079000,3492],[1551780091000,3492],[1551780102000,3492],[1551780113000,3492],[1551780125000,3492],[1551780136000,3492],[1551780147000,3492],[1551780158000,3492],[1551780170000,3492],[1551780181000,3492],[1551780192000,3492],[1551780204000,3492],[1551780215000,3492],[1551780226000,3492],[1551780238000,3492],[1551780249000,3492],[1551780260000,3492],[1551780272000,3492],[1551780283000,3491],[1551780294000,3473],[1551780305000,3465],[1551780317000,3461],[1551780328000,3459],[1551780339000,3456],[1551780351000,3450],[1551780362000,3443],[1551780373000,3437],[1551780385000,3433],[1551780396000,3427],[1551780407000,3420],[1551780418000,3411],[1551780430000,3407],[1551780441000,3405],[1551780452000,3401],[1551780464000,3400],[1551780475000,3391],[1551780486000,3384],[1551780498000,3379],[1551780509000,3370],[1551780520000,3366],[1551780531000,3362],[1551780543000,3357],[1551780554000,3351],[1551780565000,3347],[1551780577000,3344],[1551780588000,3340],[1551780599000,3331],[1551780611000,3316],[1551780622000,3310],[1551780633000,3307],[1551780644000,3304],[1551780656000,3298],[1551780667000,3294],[1551780678000,3288],[1551780690000,3283],[1551780701000,3276],[1551780712000,3270],[1551780724000,3267],[1551780735000,3260],[1551780746000,3252],[1551780757000,3249],[1551780769000,3247],[1551780780000,3243]]'

if not user.__contains__("13243"):
    pass
else:
    print("hit")
    print(user)
