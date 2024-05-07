-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 07, 2024 at 06:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `TEMP`
--

CREATE TABLE `TEMP` (
  `number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `TEMP`
--

INSERT INTO `TEMP` (`number`) VALUES
(1),
(2);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL,
  `name` text NOT NULL,
  `face_encode` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`face_encode`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`3r4
--

INSERT INTO `user` (`id`, `email`, `password`, `name`, `face_encode`) VALUES
(1, 'phuc.le@gmail.com', '123', 'Phuc', '[-0.09229973, 0.06532384, 0.04009226, -0.05365203, -0.10925896, -0.04907792, -0.03226578, -0.18599327, 0.13882522, -0.13733706, 0.23188642, -0.05568586, -0.23171236, -0.1181618, -0.08514873, 0.16635306, -0.12669459, -0.16783568, -0.03875085, -0.00070857, 0.07346141, -0.0223571, 0.02634755, 0.06007597, -0.08339832, -0.3488372, -0.13876003, -0.02472924, -0.00260636, -0.03949988, -0.04124486, 0.01393793, -0.23331501, -0.10003242, -0.01788761, 0.09079146, -0.04161066, -0.04059403, 0.16409145, -0.05337705, -0.23510988, 0.02601665, 0.08000303, 0.21954432, 0.19156583, 0.10504767, 0.02800424, -0.12315959, 0.05422737, -0.1705088, 0.07654781, 0.10981921, 0.07650129, 0.01243163, -0.01911518, -0.1596144, -0.00787841, 0.09132659, -0.13754795, 0.04958575, 0.08985483, -0.1494087, -0.03100644, -0.06330389, 0.20665504, 0.0484434, -0.07840812, -0.17434508, 0.18408181, -0.21438892, -0.06287946, 0.01708759, -0.10937802, -0.19389673, -0.3538152, 0.04715838, 0.40292194, 0.14499982, -0.14106356, 0.10283429, -0.00762762, 0.03045007, 0.10087258, 0.12148964, -0.01579232, 0.05560616, -0.15476555, 0.01680884, 0.20793869, -0.06017852, -0.04592881, 0.22147377, -0.02654973, 0.06247374, 0.08205891, 0.05300998, -0.08042246, 0.06299525, -0.15604028, 0.02685709, 0.08616482, -0.04249344, 0.03208666, 0.08088898, -0.0944068, 0.12594271, -0.05371659, 0.01758909, -0.01110797, -0.01754767, -0.14267859, -0.08515321, 0.14975879, -0.18869425, 0.21571945, 0.16784345, 0.05519527, 0.16966547, 0.18205652, 0.12463606, 0.01994379, -0.01340927, -0.19980173, -0.05611245, 0.09595586, -0.05814088, 0.19978397, 0.07858801]'),
(2, 'phuong@gmail.com', '123', 'phuong@gmail.com', '[-0.09690898656845093,0.05210242047905922,0.0627569854259491,0.034494802355766296,-0.048547398298978806,-0.01994435116648674,-0.05691729485988617,-0.09360763430595398,0.15088345110416412,-0.09603147953748703,0.21413017809391022,-0.0468406043946743,-0.20119965076446533,-0.11865238845348358,0.00047450512647628784,0.148674875497818,-0.208714097738266,-0.14640164375305176,0.043686725199222565,-0.04774952679872513,0.06704331189393997,0.008614589460194111,-0.01077267900109291,0.054063793271780014,-0.11553801596164703,-0.35015612840652466,-0.09379448741674423,-0.08445309847593307,0.04265585541725159,-0.05037490278482437,-0.07431108504533768,0.09228824079036713,-0.17082996666431427,-0.021886572241783142,0.04086457937955856,0.12731418013572693,0.029369596391916275,0.03573775291442871,0.16636605560779572,-0.019588224589824677,-0.1804186850786209,0.03271065652370453,0.030689312145113945,0.241677924990654,0.1680867224931717,0.11724063009023666,-0.08555594086647034,-0.050089068710803986,0.0639452338218689,-0.15068626403808594,0.039144717156887054,0.18146714568138123,0.1196281760931015,0.02898745983839035,0.012234922498464584,-0.15996740758419037,-0.02342565543949604,0.040455836802721024,-0.17443490028381348,-0.009996188804507256,-0.014813912101089954,-0.16300994157791138,0.007736175321042538,-0.053144123405218124,0.2266397625207901,0.05056282877922058,-0.08259106427431107,-0.1651199758052826,0.11348515003919601,-0.18391023576259613,-0.10381457209587097,0.03445693850517273,-0.10848166048526764,-0.14795488119125366,-0.33234256505966187,0.03839411586523056,0.35428524017333984,0.08764654397964478,-0.22660939395427704,0.12356811761856079,0.026053911074995995,-0.06435471028089523,0.12116675823926926,0.15518049895763397,-0.037387993186712265,0.030112694948911667,-0.10400852560997009,-0.04824128746986389,0.1471766233444214,-0.027261603623628616,-0.033945225179195404,0.15735922753810883,-0.0508958175778389,0.12907132506370544,0.058090273290872574,-0.04569389671087265,-0.03231463581323624,0.015397213399410248,-0.15393704175949097,-0.06203879415988922,0.005360995419323444,-0.011559750884771347,-0.020257581025362015,0.09017674624919891,-0.15884904563426971,0.08734650164842606,0.016913292929530144,-0.03557642549276352,-0.011801527813076973,0.04587774723768234,-0.1335655152797699,-0.0659051164984703,0.13866093754768372,-0.3121967613697052,0.22510981559753418,0.18502357602119446,0.03721598908305168,0.1716281920671463,0.09568799287080765,0.0814388319849968,-0.015622122213244438,0.00045540276914834976,-0.17334452271461487,-0.04937312379479408,0.11727653443813324,-0.073287233710289,0.10221460461616516,0.01918105222284794]'),
(3, 'qhuy@gmail.com', '123', 'qhuy', '[-0.10243828594684601,0.041645362973213196,-0.002480185590684414,-0.027290159836411476,-0.0726599469780922,-0.042753178626298904,-0.08424124121665955,-0.0983012393116951,0.10584622621536255,-0.09552497416734695,0.1673554927110672,-0.02908322960138321,-0.174357071518898,-0.09542769938707352,-0.03316425532102585,0.14214187860488892,-0.18471796810626984,-0.12004516273736954,-0.06185486167669296,-0.03542784973978996,0.0602223202586174,0.027136627584695816,0.022055134177207947,0.0653550922870636,-0.12041150033473969,-0.3777965307235718,-0.09492132067680359,-0.12194788455963135,-0.06575983762741089,-0.02358402870595455,-0.024677256122231483,0.07969358563423157,-0.17625443637371063,-0.031470946967601776,0.0603170245885849,0.12940943241119385,-0.007076815702021122,-0.002704787999391556,0.2253393530845642,-0.002595658414065838,-0.14848265051841736,0.019573304802179337,0.07093236595392227,0.28642404079437256,0.1929837167263031,0.044740237295627594,-0.001587308943271637,-0.04927845299243927,0.15636831521987915,-0.18158484995365143,0.04067464545369148,0.15544433891773224,0.03683575987815857,0.07299996167421341,0.04106856510043144,-0.10284926742315292,0.07528717070817947,0.09509553015232086,-0.14141419529914856,-0.028069650754332542,0.029231324791908264,-0.14363670349121094,-0.041382480412721634,-0.044924892485141754,0.2613958418369293,0.06409085541963577,-0.08666852861642838,-0.16386504471302032,0.0776672214269638,-0.155384823679924,-0.08385913074016571,-0.012347721494734287,-0.1992989182472229,-0.14097629487514496,-0.3603232502937317,0.049620743840932846,0.39314502477645874,0.10193178057670593,-0.16768896579742432,0.11104079335927963,-0.009252863004803658,-0.03273189440369606,0.16098356246948242,0.10453527420759201,-0.03607781231403351,0.028021832928061485,-0.08417049050331116,0.06336299329996109,0.22317485511302948,-0.03943429887294769,-0.05175649747252464,0.14196358621120453,-0.02305970899760723,0.08977550268173218,0.06973572820425034,-0.056414272636175156,-0.03584158420562744,0.0070320782251656055,-0.17465940117835999,0.06074218824505806,0.030930420383810997,-0.017278481274843216,-0.00426980247721076,0.07871508598327637,-0.15088213980197906,0.05639681965112686,0.0002689175307750702,-0.03035537153482437,-0.03913401439785957,-0.011521671898663044,-0.21754184365272522,-0.06165383756160736,0.13849176466464996,-0.2192004770040512,0.22732390463352203,0.15852327644824982,0.07789988070726395,0.14537791907787323,0.12167206406593323,0.03912819176912308,-0.040877796709537506,0.04765104502439499,-0.20174719393253326,-0.01738661341369152,0.15572574734687805,0.044220611453056335,0.10882985591888428,-0.005410932004451752]'),
(4, 'obama@gmail.com', '123', 'obama', '[-0.09143439680337906,0.13086095452308655,0.013143854215741158,-0.05788445472717285,0.01628964953124523,0.00041326507925987244,-0.08469851315021515,-0.09900523722171783,0.17989590764045715,-0.10539678484201431,0.24560223519802094,0.08059314638376236,-0.21611469984054565,-0.13486720621585846,0.04742460697889328,0.12056788057088852,-0.16367512941360474,-0.07826022058725357,-0.11224690079689026,-0.10610124468803406,0.036529477685689926,0.006349937990307808,0.10533701628446579,0.043005652725696564,-0.12117673456668854,-0.33629149198532104,-0.06974643468856812,-0.1821807324886322,-0.0015854546800255775,-0.11208320409059525,-0.09656742960214615,-0.020591991022229195,-0.18194009363651276,-0.10914110392332077,0.020732209086418152,-0.0202212855219841,0.0024095659609884024,-0.003740154206752777,0.20474016666412354,0.02820580080151558,-0.11632426828145981,0.09632833302021027,0.01547976117581129,0.21318353712558746,0.28629937767982483,0.07692298293113708,-0.011806176975369453,-0.0991305485367775,0.10386177897453308,-0.21633516252040863,0.07274052500724792,0.14290063083171844,0.08237933367490768,0.04238796979188919,0.09769628196954727,-0.1885228306055069,0.0036018341779708862,0.08834424614906311,-0.14143489301204681,0.00837215967476368,0.007887199521064758,-0.08102692663669586,-0.04035495966672897,0.038795799016952515,0.20594732463359833,0.09965956211090088,-0.12292910367250443,-0.05094441771507263,0.13211268186569214,-0.029001394286751747,0.02445152774453163,0.02434404194355011,-0.1843133419752121,-0.2006336897611618,-0.22774039208889008,0.09293822944164276,0.37345197796821594,0.19359806180000305,-0.20881180465221405,0.019557654857635498,-0.19599999487400055,0.024153146892786026,0.061056189239025116,0.00819598138332367,-0.07174452394247055,-0.13538505136966705,-0.0411863774061203,0.052821822464466095,0.0822656974196434,0.03208513557910919,-0.040988989174366,0.2150697559118271,-0.03382806479930878,0.0623677596449852,0.018536211922764778,0.05682225525379181,-0.15838755667209625,-0.03170494735240936,-0.16015227138996124,-0.06845062971115112,0.01404157467186451,-0.042036525905132294,0.030853312462568283,0.14781638979911804,-0.23243297636508942,0.0592193566262722,0.004186883568763733,-0.046667661517858505,0.02229129523038864,0.07022520899772644,-0.02721734717488289,-0.033738236874341965,0.05814214423298836,-0.23816804587841034,0.24889056384563446,0.2340346872806549,0.024954605847597122,0.17327937483787537,0.07225873321294785,0.03394286707043648,-0.016379574313759804,-0.022678084671497345,-0.182298481464386,-0.06459411233663559,0.06046797335147858,0.07552319765090942,0.08523149788379669,0.006719650700688362]');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
