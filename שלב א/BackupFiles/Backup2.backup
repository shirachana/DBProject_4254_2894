--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4 (Debian 17.4-1.pgdg120+2)
-- Dumped by pg_dump version 17.4 (Debian 17.4-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: branch; Type: TABLE; Schema: public; Owner: shira
--

CREATE TABLE public.branch (
    branchid integer NOT NULL,
    branchname character varying(100),
    blocation character varying(255),
    phone character varying(20)
);


ALTER TABLE public.branch OWNER TO shira;

--
-- Name: car; Type: TABLE; Schema: public; Owner: shira
--

CREATE TABLE public.car (
    carid integer NOT NULL,
    licenseplate integer,
    model character varying(50),
    manufacturer character varying(50),
    cyear integer,
    status character varying(20),
    priceperday numeric(10,2),
    numseats integer,
    branchid integer
);


ALTER TABLE public.car OWNER TO shira;

--
-- Name: customer; Type: TABLE; Schema: public; Owner: shira
--

CREATE TABLE public.customer (
    customerid integer NOT NULL,
    firstname character varying(50),
    lastname character varying(50),
    phone character varying(15),
    email character varying(100),
    licensenumber integer,
    dateofbirth date
);


ALTER TABLE public.customer OWNER TO shira;

--
-- Name: maintenance; Type: TABLE; Schema: public; Owner: shira
--

CREATE TABLE public.maintenance (
    maintenanceid integer NOT NULL,
    maintenancedate date,
    description character varying(255),
    mcost numeric(10,2),
    carid integer
);


ALTER TABLE public.maintenance OWNER TO shira;

--
-- Name: payment; Type: TABLE; Schema: public; Owner: shira
--

CREATE TABLE public.payment (
    paymentid integer NOT NULL,
    paymentdate date,
    amount numeric(10,2),
    paymentmethod character varying(15)
);


ALTER TABLE public.payment OWNER TO shira;

--
-- Name: rental; Type: TABLE; Schema: public; Owner: shira
--

CREATE TABLE public.rental (
    rentalid integer NOT NULL,
    startdate date,
    enddate date,
    totalcost numeric(10,2),
    customerid integer,
    carid integer,
    paymentid integer
);


ALTER TABLE public.rental OWNER TO shira;

--
-- Data for Name: branch; Type: TABLE DATA; Schema: public; Owner: shira
--

COPY public.branch (branchid, branchname, blocation, phone) FROM stdin;
1	Tel Aviv Central	Dizengoff 100, Tel Aviv	03-5551234
2	Jerusalem East	King George 23, Jerusalem	02-7778888
3	Haifa Bay	HaMifratz 12, Haifa	04-8889999
4	Lake Ianbury Branch	Felicia Lane 44110, Lake Ianbury, India	0823.387.3
5	Michaelfurt Branch	Mary Harbor 06715, Michaelfurt, Guinea	0(498)9270
6	North Carlyborough Branch	Gabriela Neck 77967, North Carlyborough, United States Minor Outlying Islands	0369935456
7	Vasquezside Branch	Harper Lights 1943, Vasquezside, New Caledonia	0723582942
8	South Emilystad Branch	Anderson Station 12191, South Emilystad, Indonesia	0015063611925x3031
9	New Justinburgh Branch	Denise Ports 336, New Justinburgh, Lebanon	0324.449.3
10	New Joshuaberg Branch	Steven Station 6211, New Joshuaberg, Sierra Leone	0878615433x37003
11	Blakeshire Branch	Donald Green 22990, Blakeshire, Uzbekistan	0103278942
12	Madisonland Branch	Nichols Trafficway 81747, Madisonland, Denmark	0+19124060
13	Port Heatherland Branch	Julia Forge 0563, Port Heatherland, Lebanon	0974.915.5
14	South Jamesbury Branch	Cheryl Village 8771, South Jamesbury, Zambia	0(617)6435
15	Lake Ericashire Branch	Everett Village 82563, Lake Ericashire, Australia	0559989318
16	Williamsport Branch	Linda Fort 558, Williamsport, Brunei Darussalam	0019989547295x3025
17	Port Katie Branch	Michael Springs 4643, Port Katie, Slovenia	0876.576.6
18	Michelleborough Branch	Washington Harbors 3049, Michelleborough, Norway	0(510)1345
19	Fosterside Branch	Hobbs Turnpike 7704, Fosterside, Equatorial Guinea	0751240605
20	Alexanderland Branch	Fuentes Via 51405, Alexanderland, Guadeloupe	0+11585622
21	Lake David Branch	Holly Crossing 46946, Lake David, Ireland	0+15067451
22	South Justinport Branch	Sanders Center 27255, South Justinport, Niger	0+11715859
23	Port Michaelhaven Branch	Timothy Alley 843, Port Michaelhaven, Western Sahara	0017269705866x809
24	West Jacob Branch	Nicholas Light 24313, West Jacob, Denmark	0487.663.0
25	Port Matthew Branch	Hicks Haven 953, Port Matthew, New Caledonia	0483845816
26	East Stuarthaven Branch	Jackson Parkways 640, East Stuarthaven, Latvia	0893439376
27	Port Roberta Branch	Thomas Shoals 1405, Port Roberta, Philippines	0149327981
28	Ramostown Branch	Pope Roads 379, Ramostown, Spain	0984072146
29	New Keithshire Branch	Alison Mission 7767, New Keithshire, Mozambique	0(343)3112
30	Port Shawn Branch	Burton Street 69846, Port Shawn, Botswana	0857029155
31	Cohenhaven Branch	Ayala Mills 891, Cohenhaven, Saint Pierre and Miquelon	0015187695193
32	Laurenton Branch	George Hills 5376, Laurenton, Andorra	0589687311
33	Brianville Branch	Tyler Estates 25495, Brianville, British Indian Ocean Territory (Chagos Archipelago)	0014950007324x8303
34	Rodriguezside Branch	Sandy Fork 48717, Rodriguezside, Jamaica	0819.833.6
35	South Brittany Branch	Swanson Neck 4510, South Brittany, Turks and Caicos Islands	0389413959
36	North Stefanie Branch	Gonzales Mountains 0709, North Stefanie, Vanuatu	0(673)3216
37	Sarahtown Branch	Smith Green 6793, Sarahtown, Anguilla	0(746)2848
38	Tylerton Branch	Kimberly Motorway 6600, Tylerton, Peru	0804965212
39	Port Stephanieburgh Branch	Rodriguez Junctions 982, Port Stephanieburgh, Sweden	0876605551
40	West Nicholas Branch	Silva Drive 04459, West Nicholas, Israel	0(578)7970
41	New Mary Branch	Jordan Common 4792, New Mary, Tanzania	0651.187.0
42	East Kathryn Branch	Olivia Shore 86470, East Kathryn, Turkmenistan	0010776591646x1859
43	Farrellfort Branch	Brian Corners 043, Farrellfort, Lao People's Democratic Republic	0245742248
44	East Vanessaton Branch	Kathleen Ridges 631, East Vanessaton, United Arab Emirates	0(143)9354
45	East Bonnie Branch	Matthew Vista 67760, East Bonnie, Zimbabwe	0364930826
46	New Brianaview Branch	Wagner Park 71281, New Brianaview, Netherlands Antilles	0+16874220
47	Gabrieltown Branch	Elizabeth Forge 8098, Gabrieltown, Senegal	0+16055976
48	Perezmouth Branch	Morgan Cliffs 0066, Perezmouth, Greece	0+17409755
49	New Sean Branch	Jordan Parks 11915, New Sean, Honduras	0012093596845x413
50	Kingshire Branch	Brenda Light 31224, Kingshire, Sweden	0(657)7208
51	Riceside Branch	Moore Crossing 65373, Riceside, Niue	0964000391
52	Armstrongberg Branch	Hayes Skyway 0825, Armstrongberg, British Virgin Islands	0392568119
53	Dickersonton Branch	Anthony Expressway 2068, Dickersonton, Ukraine	0(599)5344
54	Lake Julie Branch	Sanford Forest 094, Lake Julie, India	0+19643261
55	Sherryville Branch	Collins Rapid 95637, Sherryville, Turkey	0013484518488x63315
56	West Kim Branch	Pierce Lock 607, West Kim, Jordan	0765.194.3
57	Port Brittany Branch	Brown Via 291, Port Brittany, Ecuador	0940284704
58	New April Branch	Browning Summit 31094, New April, Nicaragua	0680786658
59	Morenohaven Branch	Huerta Shore 48762, Morenohaven, Latvia	0+17024593
60	Stanleyview Branch	Gibbs Gateway 012, Stanleyview, Northern Mariana Islands	0437284348
61	Rosstown Branch	Perez Villages 751, Rosstown, Finland	0271480106
62	Pattersonfurt Branch	Bradley Mission 172, Pattersonfurt, Cayman Islands	0208.198.4
63	Gutierrezfort Branch	Dunn Gateway 69357, Gutierrezfort, Australia	0+11977262
64	Christianmouth Branch	Hector Courts 5393, Christianmouth, Papua New Guinea	0(365)4522
65	Griffinland Branch	Phillips Ridge 8182, Griffinland, Lebanon	0+15833855
66	Jessicaburgh Branch	Taylor Field 642, Jessicaburgh, Guatemala	0545639715
67	Samanthaside Branch	Jensen Tunnel 7370, Samanthaside, Yemen	0963.770.3
68	Port Randallland Branch	Williams Isle 1073, Port Randallland, Australia	0(764)6258
69	South Abigailland Branch	Stephanie Locks 29726, South Abigailland, Zimbabwe	0+14191782
70	Timothyport Branch	Tony Bypass 728, Timothyport, Austria	0449868477x5670
71	South Allison Branch	Andrea Dale 787, South Allison, Bolivia	0+11665695
72	New Brendamouth Branch	Miller Track 86849, New Brendamouth, Georgia	0142.878.4
73	Gutierrezfort Branch	Williamson Keys 6923, Gutierrezfort, Angola	091.257.0805x9888
74	New Russellville Branch	Stevenson Parkways 85048, New Russellville, Palau	0019473841674x0922
75	North Dominique Branch	Laura Crescent 76112, North Dominique, Mauritania	0760469236
76	Kurtfurt Branch	Melanie Crossroad 224, Kurtfurt, Bahrain	0(891)0726
77	East Michael Branch	Joel Trail 5074, East Michael, Niger	036.533.2866
78	Port Marybury Branch	Morrison Motorway 87704, Port Marybury, Somalia	0+12455913
79	South Cynthia Branch	Kyle Divide 147, South Cynthia, Andorra	028.598.1816
80	South Abigailfort Branch	Perez Prairie 386, South Abigailfort, Fiji	0012295609318
81	New Kenneth Branch	Erik Port 46783, New Kenneth, Guinea-Bissau	0878160082
82	Colehaven Branch	Tyler Village 377, Colehaven, Portugal	0150720027
83	Johnland Branch	Debra Isle 731, Johnland, Israel	0652069659
84	New Anthonyview Branch	Joseph Forest 2554, New Anthonyview, Saint Pierre and Miquelon	0488.501.8
85	South Scottburgh Branch	Murillo Drive 812, South Scottburgh, Macedonia	0(133)4079
86	Reidburgh Branch	Jefferson Plains 749, Reidburgh, Slovakia (Slovak Republic)	0+15410181
87	Deannashire Branch	Mcguire Fords 51676, Deannashire, United States Virgin Islands	0716976325
88	West Travis Branch	Smith Heights 992, West Travis, Anguilla	0(155)4633
89	Robertberg Branch	Vang Road 203, Robertberg, Switzerland	0(486)7012
90	Port Tracy Branch	Laura Canyon 1134, Port Tracy, Lao People's Democratic Republic	0+17998494
91	North Marcusburgh Branch	Samantha Alley 026, North Marcusburgh, Guatemala	0130418610
92	West Joshuahaven Branch	Wolf Unions 2825, West Joshuahaven, Myanmar	0438156562
93	Port Jessicaside Branch	Ponce Port 820, Port Jessicaside, Ecuador	0+16187198
94	New Annaburgh Branch	Padilla Motorway 621, New Annaburgh, Aruba	0362479232
95	East Patrickside Branch	Robinson Islands 262, East Patrickside, Greenland	0012075015132
96	Heatherfurt Branch	Reilly Unions 24117, Heatherfurt, United States of America	0(448)1349
97	Mathewsside Branch	Watson Coves 363, Mathewsside, Tunisia	0(229)8392
98	Delgadoland Branch	Denise Knolls 3570, Delgadoland, Reunion	0(586)1055
99	Nicoleport Branch	Joseph Dale 18995, Nicoleport, Korea	0517305795
100	South Susan Branch	Coffey Skyway 673, South Susan, Montenegro	0011541635320
101	East Paulborough Branch	Rodriguez Mews 36572, East Paulborough, Uganda	0453.937.5
102	East Jonathan Branch	Alison Bypass 4020, East Jonathan, Costa Rica	0(183)1775
103	East Lisa Branch	Ashley Highway 9885, East Lisa, United States Minor Outlying Islands	0283.709.3
104	North Katelyn Branch	Ronald Lodge 439, North Katelyn, Turkmenistan	0646609851
105	Westbury Branch	Martinez Mills 22926, Westbury, Wallis and Futuna	0171.338.1
106	South Michael Branch	Burns Mews 9048, South Michael, Niue	0263408054
107	West Diana Branch	Jill Track 37012, West Diana, United States Virgin Islands	0(398)2787
108	North Rodneychester Branch	Ortega Grove 7114, North Rodneychester, Guinea	0019971740496x3026
109	Lake Marystad Branch	Durham Locks 379, Lake Marystad, Montenegro	0861995461
110	East Frankview Branch	Coleman Vista 63327, East Frankview, Burundi	0817.784.6
111	Woodardfurt Branch	Davis Spurs 432, Woodardfurt, Isle of Man	0(548)3082
112	Port Kathleen Branch	Morales Estates 27284, Port Kathleen, Palestinian Territory	0013246212995x5279
113	South George Branch	Karen Mountain 97454, South George, Holy See (Vatican City State)	0+10532933
114	East Eric Branch	Howard Bypass 438, East Eric, Marshall Islands	0310238402
115	Candicebury Branch	Jasmine Haven 3645, Candicebury, Trinidad and Tobago	0+11317238
116	Pacebury Branch	Turner Square 01004, Pacebury, Bouvet Island (Bouvetoya)	0(887)3092
117	Donaldchester Branch	Amanda Garden 15429, Donaldchester, Germany	0017592909686x198
118	Bryanton Branch	Randy Common 391, Bryanton, Cameroon	0+13650846
119	Codytown Branch	Thomas Pike 9965, Codytown, Djibouti	0473934784
120	Dixonview Branch	Hamilton Expressway 8358, Dixonview, Gabon	0(885)6437
121	Nguyenstad Branch	Melissa Parkway 4049, Nguyenstad, Uzbekistan	0+12503650
122	Willismouth Branch	Gregory Drive 9231, Willismouth, Antigua and Barbuda	0+11065459
123	Lake Graceview Branch	Wilkins Keys 624, Lake Graceview, Hungary	0015124763298x95851
124	West Julian Branch	Rachel Drive 010, West Julian, Cook Islands	0(144)0894
125	South Veronicamouth Branch	Campbell Plain 0966, South Veronicamouth, Guadeloupe	0(149)1722
126	Lake Cheryl Branch	Courtney Meadow 22059, Lake Cheryl, Dominican Republic	0866.671.2
127	Margaretmouth Branch	Steven Fall 97716, Margaretmouth, Faroe Islands	0+12601991
128	Matthewport Branch	Audrey Wall 68565, Matthewport, Bhutan	0018777316427
129	Danielchester Branch	Vanessa Hill 6337, Danielchester, Cayman Islands	0321400812
130	North Amy Branch	Miller Branch 4380, North Amy, Jamaica	0812706614
131	Russellton Branch	Duarte Rapids 57279, Russellton, Kiribati	039.701.9567
132	Samanthaview Branch	Sheryl Skyway 16008, Samanthaview, Finland	0116792160x803
133	Lake Kaylaberg Branch	Randy Walk 18958, Lake Kaylaberg, Germany	0+17039182
134	Tammyhaven Branch	Julie Manors 0291, Tammyhaven, Cape Verde	0(738)8193
135	Lake Micheleborough Branch	Webb Canyon 00668, Lake Micheleborough, United Kingdom	0263.619.1
136	Nicoleshire Branch	Joel Branch 8354, Nicoleshire, China	0694.702.2
137	North Danaburgh Branch	Benjamin Dale 1362, North Danaburgh, Kiribati	0906339226
138	Franklinport Branch	Jones Drive 9056, Franklinport, Marshall Islands	0649.613.3
139	Port Alexandra Branch	Grant Branch 164, Port Alexandra, Northern Mariana Islands	0+17592502
140	Nguyenborough Branch	Tyler Stravenue 730, Nguyenborough, New Caledonia	0010029709068x3809
141	Michaelfurt Branch	Miller Cove 7467, Michaelfurt, Guinea-Bissau	0697860368
142	New Michaelstad Branch	Tran Rapid 22296, New Michaelstad, Pakistan	0+16938222
143	New Crystalfort Branch	Anderson Island 210, New Crystalfort, Colombia	0+14773139
144	Karistad Branch	Hendricks Highway 58148, Karistad, Jordan	0+11497084
145	New Joshuaton Branch	Brown Radial 591, New Joshuaton, Saint Vincent and the Grenadines	0012762580279x461
146	Danielmouth Branch	Young Haven 290, Danielmouth, Nauru	0317.552.4
147	Clarkborough Branch	Charles Freeway 7168, Clarkborough, Somalia	0(977)0106
148	Samuelburgh Branch	Glover Pine 9974, Samuelburgh, Lao People's Democratic Republic	0(424)3859
149	Port Derrickmouth Branch	Colon Pine 8209, Port Derrickmouth, Congo	042.295.2253x131
150	Michaelbury Branch	Ward Manors 103, Michaelbury, Korea	0879736720
151	Frankbury Branch	Joseph Prairie 3512, Frankbury, Iraq	0+11850795
152	South Jacqueline Branch	Leroy Cove 16052, South Jacqueline, Indonesia	0(445)2566
153	North Victoria Branch	Jason Key 08364, North Victoria, Palau	0875.564.8
154	South Craigchester Branch	Johnson Mountain 7908, South Craigchester, Bulgaria	0279.180.2
155	Ivanport Branch	Hopkins Knoll 705, Ivanport, Tunisia	0+19772876
156	Valeriefurt Branch	Stewart Trail 80618, Valeriefurt, Guernsey	0+19545607
157	North Jofurt Branch	Barajas Shoals 377, North Jofurt, Guam	0(613)5189
158	South Jamesfurt Branch	Paul Burg 3787, South Jamesfurt, Central African Republic	0999482657
159	Teresatown Branch	Janice Burg 7602, Teresatown, Burundi	0+10477204
160	Jimenezfurt Branch	Richard Creek 67000, Jimenezfurt, Sweden	0011390704019x9072
161	Allenchester Branch	Maria Flat 59302, Allenchester, Norway	0(137)2618
162	New Cory Branch	Kimberly Summit 47327, New Cory, Spain	0+18650446
163	East Rebecca Branch	John Prairie 7408, East Rebecca, Korea	0+15842570
164	Lake Zachary Branch	Frederick Fields 6014, Lake Zachary, Morocco	0566.914.0
165	Timothymouth Branch	Calvin Burgs 33477, Timothymouth, Cameroon	0017874836644
166	Adamshaven Branch	Debbie Parks 043, Adamshaven, Monaco	0735.585.5
167	New Joshua Branch	Michael Ridges 77801, New Joshua, Jordan	0017796121003x11078
168	East Matthewborough Branch	Burke Avenue 03523, East Matthewborough, Cocos (Keeling) Islands	0+14742502
169	North Carolbury Branch	Pierce Prairie 6159, North Carolbury, Greece	0505473100
170	South Angiechester Branch	Charlotte Station 257, South Angiechester, Bahamas	0699.932.0
171	South Jacob Branch	Ellen Square 730, South Jacob, Uganda	0(653)5830
172	North Micheleport Branch	Jennifer Ports 248, North Micheleport, Honduras	0(915)2411
173	Kathyton Branch	Mary Inlet 35380, Kathyton, Azerbaijan	0558175618
174	Tracytown Branch	Fisher Glens 6652, Tracytown, Ghana	0870713859
175	West Michelle Branch	Sean Parkways 955, West Michelle, Burundi	0+19191005
176	West Francisco Branch	Contreras Highway 144, West Francisco, New Zealand	0+16480691
177	Wallaceshire Branch	Annette Center 502, Wallaceshire, Egypt	0013506390008x808
178	Port Michael Branch	Diane Route 1955, Port Michael, Tajikistan	0443227541x5902
179	South Mistyview Branch	Alexander Loop 684, South Mistyview, Kenya	0(472)5558
180	Lake Nicoleville Branch	Lisa Shores 47156, Lake Nicoleville, Grenada	0(866)0899
181	North Joshua Branch	Thomas Harbors 0333, North Joshua, British Virgin Islands	0(553)8938
182	South Jennifer Branch	Mark Ridges 525, South Jennifer, Switzerland	0666.500.6
183	Shelbyfort Branch	Alexander Camp 32622, Shelbyfort, Georgia	0739.849.9
184	Johnsonland Branch	John Ramp 0366, Johnsonland, Saint Martin	0013922994564x1129
185	South Jason Branch	Berry Row 0689, South Jason, Philippines	0010348520504x03386
186	East Jasonberg Branch	Bobby Burg 893, East Jasonberg, Costa Rica	0+19687736
187	New Frederickchester Branch	Christian Ports 1151, New Frederickchester, Belgium	0314688881
188	New Fredbury Branch	Trevino Tunnel 4929, New Fredbury, Aruba	0978.927.4
189	North Jennifer Branch	Jeffrey Inlet 493, North Jennifer, Bahamas	0(759)8185
190	Amberfort Branch	Ortega Circle 353, Amberfort, Norfolk Island	0(728)0366
191	East Jenniferhaven Branch	Sutton Course 53650, East Jenniferhaven, Fiji	0922.780.0
192	West Christopherland Branch	Ball Well 92448, West Christopherland, Belize	0326.157.3
193	North Wesley Branch	Brown Circle 4860, North Wesley, Korea	0186.599.0
194	Emilyside Branch	Daniel Land 7635, Emilyside, Italy	0192.829.3
195	Douglasfort Branch	Lisa Lights 91473, Douglasfort, Hungary	0152024848
196	North Markhaven Branch	Joseph Pine 08229, North Markhaven, Solomon Islands	0015742473553x038
197	Tonyborough Branch	Pamela Drives 325, Tonyborough, Bolivia	0(262)2213
198	Moodystad Branch	Nash Bridge 631, Moodystad, Bahrain	0+19828103
199	Markfurt Branch	Smith Circle 7042, Markfurt, Libyan Arab Jamahiriya	0328177145
200	Port Teresa Branch	Megan Loaf 484, Port Teresa, Austria	0722.221.4
201	Andersonhaven Branch	Jason Ranch 2510, Andersonhaven, Tunisia	0120501712
202	Curtismouth Branch	Campbell Common 480, Curtismouth, Guinea	0(986)5312
203	Nicholasberg Branch	Victoria Valleys 979, Nicholasberg, Guyana	0012095688331x920
204	New Jose Branch	Mendez Pass 615, New Jose, Tonga	0(810)7642
205	Johnland Branch	Mayer Port 465, Johnland, Guadeloupe	0016828934941
206	Brookefort Branch	Chan Cliffs 99734, Brookefort, Bermuda	0(530)8410
207	South Kellyview Branch	Joshua Club 197, South Kellyview, Sri Lanka	0126.550.8
208	New Troymouth Branch	Underwood Station 14265, New Troymouth, Uzbekistan	0434.381.3
209	Brendatown Branch	Lopez Drive 7973, Brendatown, Portugal	0010182574225x6436
210	East David Branch	Anne Forges 6261, East David, Micronesia	0+10942292
211	New Courtney Branch	Castillo Lock 401, New Courtney, India	0231812372
212	Dixonland Branch	John Lake 97908, Dixonland, Cayman Islands	0+17831266
213	Mitchelltown Branch	Jo Court 0715, Mitchelltown, Argentina	0225.983.5
214	Zamoraton Branch	Flores Estate 272, Zamoraton, Norfolk Island	0669600726
215	North Jimmy Branch	James Mountains 819, North Jimmy, Nicaragua	0019373094474x344
216	Sullivanside Branch	Laura Field 517, Sullivanside, Jamaica	0419647877
217	Brianmouth Branch	Christopher Burgs 7508, Brianmouth, Algeria	0(655)6864
218	New Leeland Branch	Baker Ports 619, New Leeland, Belarus	0278665614
219	Lake Ellen Branch	John Plain 0615, Lake Ellen, Azerbaijan	0019940672298
220	South Anthonystad Branch	Tanner Meadow 17243, South Anthonystad, New Zealand	0(880)3880
221	Lake Dylanchester Branch	Brendan Estates 5524, Lake Dylanchester, Papua New Guinea	0685.416.0
222	Timothybury Branch	Lee Fork 93147, Timothybury, Iraq	0323.412.5
223	East Juantown Branch	Jimmy Bridge 899, East Juantown, Macedonia	0(568)7396
224	West Ivan Branch	Ryan Stravenue 4069, West Ivan, Guernsey	0+12278600
225	New Jason Branch	Sarah Falls 20875, New Jason, Ghana	0(432)8501
226	West Kelsey Branch	Sanchez Extension 85926, West Kelsey, Sri Lanka	0(216)9734
227	North Leahberg Branch	Bell Loaf 0749, North Leahberg, Bulgaria	0(867)9555
228	New Andrea Branch	James Pine 009, New Andrea, Solomon Islands	0741.542.1
229	Smithshire Branch	Black Isle 4857, Smithshire, Honduras	0618.907.5
230	Keithfort Branch	Brady Mountain 39406, Keithfort, Vanuatu	0+11821994
231	Meganmouth Branch	Page Courts 649, Meganmouth, Montenegro	0(698)9702
232	Escobarview Branch	Claudia Cliffs 727, Escobarview, Bermuda	016.687.5759x747
233	North Kathleen Branch	Anna Meadow 867, North Kathleen, Switzerland	0833281400
234	Browntown Branch	Taylor Isle 374, Browntown, Myanmar	0016296560611x26612
235	Lake Joymouth Branch	Huff Park 5846, Lake Joymouth, Central African Republic	0708.809.6
236	Kingstad Branch	Alexander Islands 047, Kingstad, Bouvet Island (Bouvetoya)	0(403)8841
237	West James Branch	Katherine Lights 93291, West James, Holy See (Vatican City State)	0888908241
238	North Evelyn Branch	Freeman Manors 1086, North Evelyn, Cape Verde	0295613502
239	Daleton Branch	Sharon Extensions 16974, Daleton, Macao	0+17190628
240	New Brandonchester Branch	Wise Street 020, New Brandonchester, Bangladesh	0(444)8847
241	Bakermouth Branch	Mays Islands 0325, Bakermouth, Guyana	0(191)5113
242	East Kim Branch	Robert Manor 89623, East Kim, Kuwait	0(377)9324
243	Louismouth Branch	Reginald Stream 17307, Louismouth, Pitcairn Islands	0464384259
244	Lake Timothy Branch	Michael Landing 28724, Lake Timothy, Madagascar	0(126)9173
245	Markside Branch	Brooks Valleys 268, Markside, Australia	0130.302.9
246	South Brianstad Branch	Hooper Hollow 81104, South Brianstad, Greece	0755372012
247	East Makayla Branch	Tina Route 548, East Makayla, Macao	0+19096102
248	Navarroborough Branch	Jeffrey Fork 515, Navarroborough, Israel	0569.567.8
249	Maryton Branch	Lane Path 35323, Maryton, Saint Barthelemy	0(099)4184
250	Stevetown Branch	Cynthia Fords 0202, Stevetown, Antarctica (the territory South of 60 deg S)	0(202)3833
251	Shepardburgh Branch	Brian Summit 4273, Shepardburgh, Saudi Arabia	0775899824
252	Mitchellbury Branch	Katelyn Club 488, Mitchellbury, Svalbard & Jan Mayen Islands	0020498617x782
253	North Erikberg Branch	Wayne Parkway 2670, North Erikberg, Brazil	0258696392
254	East Patrick Branch	Young Drives 300, East Patrick, Estonia	0(838)5182
255	North Kelly Branch	Evans Stream 7059, North Kelly, Iran	0298173170
256	Wilsonton Branch	Cole Lane 3416, Wilsonton, Sierra Leone	0966.554.3
257	Kristymouth Branch	Frazier Mills 2446, Kristymouth, Taiwan	0449691217
258	West Monica Branch	Taylor Spurs 56842, West Monica, Equatorial Guinea	0394.233.3
259	North Dawnville Branch	Stephanie Curve 74056, North Dawnville, Mali	0+14896224
260	Anthonyberg Branch	Tucker Road 677, Anthonyberg, Kyrgyz Republic	0114131273
261	Lake Terrifort Branch	King Vista 5360, Lake Terrifort, Estonia	0244604457
262	Briannashire Branch	White Crest 115, Briannashire, Niger	0+12963797
263	Edwardmouth Branch	Harrison Forges 45605, Edwardmouth, Ecuador	0861445866
264	Katherineton Branch	Bowen Ridge 9871, Katherineton, Dominica	0(206)0267
265	North Megan Branch	Chen Station 3518, North Megan, Marshall Islands	0(675)1240
266	Fordville Branch	Holmes Mill 3705, Fordville, El Salvador	0317.145.4
267	Port Jessica Branch	Katie Islands 1340, Port Jessica, Belarus	0019130428320x3025
268	Port Daniellechester Branch	Nelson Crescent 87489, Port Daniellechester, Iraq	0108551390
269	Lake Alexanderville Branch	Buckley Lights 72113, Lake Alexanderville, Bolivia	0(244)5630
270	Stephenton Branch	Mary Walks 94652, Stephenton, Bulgaria	0+13176647
271	Tinastad Branch	Austin Forks 9041, Tinastad, Hong Kong	0018343886590x40582
272	New Lucas Branch	Shah Harbor 08332, New Lucas, Estonia	0176462491
273	Lake Betty Branch	Nicholas Motorway 82178, Lake Betty, Seychelles	0510012148
274	North Julie Branch	Huerta Alley 58471, North Julie, Montenegro	0(792)6823
275	New Joseph Branch	Geoffrey Lock 4856, New Joseph, Reunion	0010928481571x941
276	East Richard Branch	Lopez Turnpike 89504, East Richard, Faroe Islands	0019822597815x84164
277	Lake Emma Branch	Woodward Junction 283, Lake Emma, Antigua and Barbuda	0018086038468x23152
278	Angelachester Branch	Calderon Rapid 234, Angelachester, Bosnia and Herzegovina	0165190903
279	Reynoldsfort Branch	Kara View 246, Reynoldsfort, Lithuania	0932201634
280	New Ginaton Branch	Timothy Passage 615, New Ginaton, Malaysia	0650813898
281	New Samanthatown Branch	Alicia Isle 418, New Samanthatown, Guinea	0950552872
282	Lauriemouth Branch	Christopher Walks 9736, Lauriemouth, Kyrgyz Republic	0(616)2310
283	Dennisview Branch	Berg Parkway 82818, Dennisview, Sudan	0688.516.7
284	Rebeccaburgh Branch	Deborah Fall 5800, Rebeccaburgh, Comoros	0175866712
285	Adamsfurt Branch	Gonzalez Gateway 4846, Adamsfurt, Ecuador	0459633038
286	Morganville Branch	Barry Mountains 15635, Morganville, Sri Lanka	0+15846134
287	East Amy Branch	Karen Brooks 1886, East Amy, Macao	072.219.3427x8092
288	Lewisville Branch	Garner Club 1108, Lewisville, Tokelau	0382467750
289	Lake Travis Branch	Ryan Forge 776, Lake Travis, Mozambique	0629607627
290	West Yolandamouth Branch	Snyder Courts 60665, West Yolandamouth, Belgium	0524516958
291	Lake Matthew Branch	Arnold Courts 972, Lake Matthew, Gabon	0781667871
292	Burtonstad Branch	Williams Mission 1675, Burtonstad, Antarctica (the territory South of 60 deg S)	0+16533473
293	West Brendanview Branch	Jennifer Light 0146, West Brendanview, Kenya	0899.341.3
294	Port Linda Branch	Charles Dale 83203, Port Linda, Indonesia	0(259)7404
295	New Theresa Branch	Day Mews 6782, New Theresa, Lithuania	0+15189240
296	North Annashire Branch	Heather Tunnel 27918, North Annashire, Mongolia	0012868951284x797
297	Josephshire Branch	Kayla Harbors 6310, Josephshire, Egypt	0932489833
298	Laurashire Branch	Mackenzie Throughway 29860, Laurashire, Guadeloupe	0(754)5781
299	North Marissa Branch	Michael Plaza 31105, North Marissa, Malawi	0404087824
300	Smithfort Branch	Castaneda Mills 36363, Smithfort, Fiji	0430.172.9
301	Kevinstad Branch	White Neck 036, Kevinstad, Reunion	0(050)0151
302	Tamarachester Branch	Barker Views 17254, Tamarachester, Chad	0015078806257x024
303	South Christopher Branch	Campbell Avenue 69982, South Christopher, Swaziland	0010120702787
304	Port Catherine Branch	Hayes Stravenue 7251, Port Catherine, Uganda	0015667745393x395
305	Lake Patrick Branch	Baker Trail 16135, Lake Patrick, Portugal	0(803)2379
306	Timothymouth Branch	Miller Station 90712, Timothymouth, Guatemala	0419530539
307	Stephenview Branch	Byrd Course 796, Stephenview, Tanzania	0+13873688
308	Robinsonshire Branch	Wood Harbor 11752, Robinsonshire, British Virgin Islands	0+15280271
309	Lake Patricia Branch	Dennis Summit 306, Lake Patricia, Turkmenistan	0013542669992x323
310	Harrisville Branch	Ramos Ways 2540, Harrisville, Malawi	0+10640830
311	New Autumn Branch	Sanford Park 429, New Autumn, Indonesia	0010947818017x69101
312	Lake Michaelland Branch	Wheeler Terrace 607, Lake Michaelland, Kyrgyz Republic	0(598)7354
313	West Joshuaside Branch	Martin Squares 738, West Joshuaside, Brazil	0824.307.0
314	Jacobside Branch	Chung Highway 62949, Jacobside, New Caledonia	0(351)0472
315	Wattsville Branch	Wright Brook 83469, Wattsville, Chad	0014862786662
316	Sandovalshire Branch	Ashley Glens 055, Sandovalshire, Turkmenistan	0161.040.2
317	East Robertville Branch	King Extension 0819, East Robertville, Greece	0968.178.8
318	Alexanderstad Branch	Daniel Neck 1678, Alexanderstad, Taiwan	0117.746.3
319	Lake Thomas Branch	Hanna Creek 377, Lake Thomas, Grenada	0283259312
320	Port Sarah Branch	Bailey Road 527, Port Sarah, Gambia	0(531)3914
321	North Marcusview Branch	Watson Keys 178, North Marcusview, Ethiopia	0(451)9554
322	South Kevin Branch	Nunez Village 35576, South Kevin, Nepal	063.182.7868x8620
323	Martinborough Branch	Richard Crossing 8688, Martinborough, Bouvet Island (Bouvetoya)	0014582445340x07983
324	North Caitlin Branch	Young Estate 71598, North Caitlin, Congo	0702627000
325	East Heatherside Branch	Watts Common 026, East Heatherside, Svalbard & Jan Mayen Islands	0014709845653x77489
326	Port Sean Branch	Patrick Fords 5120, Port Sean, Guyana	0(339)8794
327	Coreymouth Branch	Clark Lake 84917, Coreymouth, Costa Rica	0+12827612
328	Mccoystad Branch	Kenneth Union 90921, Mccoystad, Cocos (Keeling) Islands	0+17795224
329	South Scotttown Branch	Mikayla Forge 546, South Scotttown, Cape Verde	0016852480393x49643
330	Kirkmouth Branch	Rocha Knolls 260, Kirkmouth, Spain	0013782146387x4756
331	North Tracy Branch	Lynn Course 2440, North Tracy, Congo	0(758)6885
332	South Shannontown Branch	Reed Glen 26562, South Shannontown, Russian Federation	0(025)0802
333	East William Branch	Davis Dam 95612, East William, China	0697542857
334	Romanville Branch	Cruz Flat 1499, Romanville, Togo	0785.271.9
335	Saraside Branch	Jorge Neck 690, Saraside, Jamaica	0016899934242x259
336	New Jeffrey Branch	Lauren Corner 039, New Jeffrey, Northern Mariana Islands	0303456702x81988
337	Heatherberg Branch	Greer Common 97514, Heatherberg, Grenada	0830076563x412
338	Crystalton Branch	Davis Fork 35286, Crystalton, Barbados	0765756359
339	East Jacob Branch	Green Plaza 252, East Jacob, Netherlands	0929199744
340	Kathymouth Branch	Smith Ferry 726, Kathymouth, United Kingdom	0673509526
341	Beasleyland Branch	David Lock 4040, Beasleyland, Pakistan	0(140)8734
342	Lake Heather Branch	Lyons Field 74117, Lake Heather, Ireland	0116006375
343	Charleston Branch	William Forge 11413, Charleston, Cambodia	0(073)8938
344	Sethport Branch	Elizabeth Glen 672, Sethport, Costa Rica	0705.430.9
345	Ashleemouth Branch	Smith Terrace 04143, Ashleemouth, France	0(876)5543
346	Watsonland Branch	Smith Place 9396, Watsonland, China	0438.976.3
347	Lake Saraview Branch	Paul Ferry 188, Lake Saraview, Tajikistan	0(940)8228
348	South Miranda Branch	Alvarez Underpass 4058, South Miranda, Saint Barthelemy	0+13646027
349	Campbellfort Branch	Schroeder Alley 0582, Campbellfort, Greenland	0838479968
350	Brucechester Branch	Schroeder Shore 4834, Brucechester, Netherlands	0(586)3837
351	West Courtneyland Branch	Nicole Shore 618, West Courtneyland, Slovakia (Slovak Republic)	0016632954728
352	Richardview Branch	Linda Way 00435, Richardview, Northern Mariana Islands	0(076)5538
353	Christinechester Branch	Hall Ford 59551, Christinechester, Myanmar	0431.588.7
354	East Tylerport Branch	Welch Stream 0606, East Tylerport, United States Minor Outlying Islands	0+10988163
355	Garciaborough Branch	Davis Forge 9186, Garciaborough, Norway	0(559)9668
356	Brittneychester Branch	Veronica Manor 76454, Brittneychester, Argentina	0014410060705x4925
357	Olsenborough Branch	Cory Mall 1806, Olsenborough, Finland	0(750)9947
358	Port Nicole Branch	Joshua Corners 67109, Port Nicole, Portugal	0152614853
359	East Markville Branch	Elijah Heights 436, East Markville, Ecuador	0665376135
360	New Davidberg Branch	Ho Tunnel 8095, New Davidberg, Lesotho	0(976)8844
361	Taraborough Branch	Velasquez Mountain 6075, Taraborough, Iran	0102.070.5
362	Robertville Branch	Catherine Ridge 34667, Robertville, Cuba	0(362)7565
363	South Nicoleville Branch	Eileen Plaza 26697, South Nicoleville, Tonga	0(147)5967
364	East Edward Branch	Singleton Rapids 03726, East Edward, Yemen	0011247107063x02619
365	Smithburgh Branch	Chad Center 41629, Smithburgh, Nigeria	0+12329993
366	Duncanfurt Branch	Micheal Parkway 7645, Duncanfurt, Uganda	0+18725335
367	Johnnyshire Branch	Jeremy Vista 674, Johnnyshire, Samoa	0+15254605
368	Travisstad Branch	Brittany Forge 58289, Travisstad, Holy See (Vatican City State)	0+11892845
369	West Christopherland Branch	Michelle Cliff 1398, West Christopherland, Marshall Islands	0014985022885x327
370	Lake Victoria Branch	John Loop 928, Lake Victoria, American Samoa	0+12784858
371	Corteztown Branch	Steven Causeway 6480, Corteztown, Libyan Arab Jamahiriya	0017607967352x1753
372	New Melodyburgh Branch	Anita Canyon 06479, New Melodyburgh, Belize	0217533921
373	South Steve Branch	White Mountains 940, South Steve, India	0626809687
374	Christianborough Branch	Amanda Underpass 61187, Christianborough, Tonga	0+10269987
375	Alyssabury Branch	Heather Cove 80918, Alyssabury, Samoa	0850.246.5
376	Lawrenceton Branch	Miller Neck 653, Lawrenceton, Gibraltar	0010913441059x71638
377	North Nancy Branch	Stephen Fields 38303, North Nancy, Macedonia	0011875389929x65948
378	Lake Matthewberg Branch	Nathan Garden 00949, Lake Matthewberg, Hong Kong	0(029)7776
379	East Renee Branch	Angela Viaduct 5668, East Renee, Zambia	0555038723
380	New Loriville Branch	John River 308, New Loriville, Kyrgyz Republic	0568.940.2
381	East Josephberg Branch	John Island 4823, East Josephberg, Cote d'Ivoire	0832605241
382	Sanchezfurt Branch	Brown Wells 6853, Sanchezfurt, Cambodia	0554.176.1
383	Lake Michele Branch	Shelley Canyon 648, Lake Michele, Panama	0+16565940
384	Steelechester Branch	Morrison Ford 633, Steelechester, Macao	0(441)4001
385	Jessicaburgh Branch	Bethany Overpass 5884, Jessicaburgh, Timor-Leste	0015375341950x74643
386	Ashleybury Branch	Wells Keys 71095, Ashleybury, Thailand	0011021278882
387	Alexandraborough Branch	Russo Harbors 799, Alexandraborough, Hungary	0542793491
388	West Bruce Branch	Garcia Tunnel 48255, West Bruce, Korea	0+15100261
389	Lake Carolstad Branch	Leslie Square 3192, Lake Carolstad, San Marino	0648157293
390	Heathhaven Branch	Todd Parkways 001, Heathhaven, Palestinian Territory	0220.153.2
391	Lake Mariemouth Branch	Tammy Forges 34281, Lake Mariemouth, Madagascar	0+19273784
392	South Kristen Branch	Melissa Light 586, South Kristen, Ecuador	0974868192x241
393	East Elizabethberg Branch	Cook Crossroad 2230, East Elizabethberg, Cayman Islands	0(024)2765
394	Hannahfort Branch	Ryan Vista 130, Hannahfort, Colombia	0+16693575
395	North Brianstad Branch	Brittany Terrace 96629, North Brianstad, Liberia	0932436226
396	South Damon Branch	Robert Island 1620, South Damon, Sao Tome and Principe	0956.466.9
397	Port Marktown Branch	Burns Loop 0574, Port Marktown, Hong Kong	0(588)9060
398	East April Branch	Brian Expressway 84019, East April, Gibraltar	0(541)3878
399	West Jessicaville Branch	Sampson Coves 5744, West Jessicaville, Guam	0017309791328
400	Lake Kaitlin Branch	Barry Neck 842, Lake Kaitlin, Guinea-Bissau	0+10416619
401	Laurafort Branch	Garcia Wells 68794, Laurafort, Sierra Leone	0781.466.9
402	New Danielmouth Branch	Robinson Road 0784, New Danielmouth, Bermuda	0319.694.2
403	Brandonstad Branch	Crystal Common 9351, Brandonstad, Saint Martin	0+17997159
\.


--
-- Data for Name: car; Type: TABLE DATA; Schema: public; Owner: shira
--

COPY public.car (carid, licenseplate, model, manufacturer, cyear, status, priceperday, numseats, branchid) FROM stdin;
1	1111111	Corolla	Toyota	2020	Available	130.00	5	1
2	2222222	Civic	Honda	2019	Rented	150.00	5	2
3	3333333	Model 3	Tesla	2021	In Maintenance	300.00	5	3
4	4587284	E-Class	Mercedes-Benz	1992	In Maintenance	194.09	4	286
5	1650495	MKZ	Lincoln	2008	In Maintenance	366.36	9	291
6	4550197	Spyder	Maserati	1989	Available	387.09	4	285
7	8485335	Maxima	Nissan	2011	In Maintenance	429.81	4	70
8	5022624	Riviera	Buick	1998	In Maintenance	239.36	5	215
9	7321343	Pathfinder	Nissan	1993	Available	367.63	5	195
10	5867706	Minx Magnificent	Hillman	1950	Rented	163.56	7	296
11	3440488	G	Infiniti	1999	Rented	245.45	9	377
12	3395169	Avalon	Toyota	2004	Available	491.96	4	35
13	7838679	MPV	Mazda	1993	Available	280.88	12	139
14	8166195	Z3	BMW	1997	Available	123.42	4	336
15	2362426	Seville	Cadillac	1994	Available	205.77	12	73
16	9207302	DBS	Aston Martin	2009	In Maintenance	253.73	2	385
17	7227755	Suburban 2500	GMC	1997	Rented	439.56	9	220
18	5258272	NSX	Acura	2003	Rented	157.88	2	394
19	3969286	SL-Class	Mercedes-Benz	1999	Rented	232.27	12	178
20	1742683	E-Class	Mercedes-Benz	1991	In Maintenance	162.92	5	318
21	2283264	Silverado Hybrid	Chevrolet	2006	Rented	442.94	4	124
22	7092382	Aviator	Lincoln	2004	In Maintenance	191.32	2	199
23	8774542	Outlook	Saturn	2010	Available	280.73	4	245
24	9000945	Corolla	Toyota	1996	Available	357.74	2	139
25	7984881	Challenger	Mitsubishi	1999	In Maintenance	225.61	4	378
26	3847845	Silverado 1500	Chevrolet	2012	Available	218.39	2	194
27	6672977	Silverado	Chevrolet	2001	Rented	376.15	2	400
28	1890954	Optima	Kia	2008	Available	483.17	9	25
29	4838250	MKZ	Lincoln	2012	Available	230.76	7	361
30	2078130	Uplander	Chevrolet	2005	In Maintenance	217.94	7	274
31	8780656	L300	Mitsubishi	1989	Rented	130.98	9	158
32	2009881	Continental	Lincoln	1988	In Maintenance	351.63	4	248
33	4198374	Acadia	GMC	2011	Rented	337.05	9	241
34	4362667	Seville	Cadillac	1995	In Maintenance	172.39	2	86
35	5015638	Corolla	Toyota	2005	Available	233.74	2	180
36	1066787	SVX	Subaru	1993	Available	494.58	4	228
37	7072085	Insight	Honda	2005	Available	288.37	7	390
38	4641001	Dakota	Dodge	2003	Rented	331.54	9	245
39	8359773	Expedition	Ford	1998	In Maintenance	221.55	2	40
40	5531013	MDX	Acura	2002	Available	202.32	5	228
41	8892251	Intrepid	Dodge	2004	Available	439.07	7	132
42	9520883	Miata MX-5	Mazda	1999	Available	341.32	12	263
43	2247985	Camaro	Chevrolet	1999	Rented	326.75	2	212
44	7012668	Canyon	GMC	2010	In Maintenance	198.27	2	258
45	8959817	Elantra	Hyundai	2001	In Maintenance	317.08	2	174
46	7169288	HHR	Chevrolet	2009	Available	160.55	5	310
47	1755420	Passat	Volkswagen	2005	In Maintenance	374.61	9	41
48	3244468	Legacy	Subaru	2005	Rented	418.43	2	210
49	7768552	PT Cruiser	Chrysler	2009	In Maintenance	235.05	12	370
50	1986786	Metro	Geo	1997	Available	313.70	9	211
51	3208440	V70	Volvo	2000	In Maintenance	453.94	7	284
52	7352261	240	Volvo	1993	In Maintenance	183.73	4	284
53	9798631	Grand Cherokee	Jeep	1996	In Maintenance	339.64	7	168
54	1804741	911	Porsche	1994	Rented	430.94	7	273
55	7347597	Tempo	Ford	1993	In Maintenance	217.55	9	66
56	1645531	Tracker	Geo	1996	Available	207.01	7	173
57	3147778	Stratus	Dodge	1995	Rented	247.96	5	259
58	5134609	Ciera	Oldsmobile	1994	In Maintenance	318.17	7	371
59	8229353	Carrera GT	Porsche	2004	Rented	347.72	7	116
60	9500583	RSX	Acura	2003	Rented	316.80	2	83
61	4877228	Seville	Cadillac	2004	In Maintenance	462.73	7	178
62	4915337	GTO	Mitsubishi	1995	In Maintenance	338.46	12	79
63	1472117	Sentra	Nissan	2007	Rented	264.67	5	114
64	2305817	Passat	Volkswagen	1988	Rented	259.09	9	361
65	8090701	SJ	Suzuki	1990	Rented	180.36	7	372
66	2355152	Vitara	Suzuki	2004	Rented	455.09	2	256
67	9672217	Mentor	Kia	1997	Rented	338.84	4	399
68	9333902	Vandura G3500	GMC	1996	Rented	240.22	9	387
69	2115673	Tacoma	Toyota	2002	Available	104.02	9	257
70	9320281	Venture	Chevrolet	2005	Rented	385.58	12	139
71	9462572	CR-V	Honda	2011	In Maintenance	172.87	12	343
72	8386751	GTI	Volkswagen	1996	In Maintenance	134.10	9	335
73	6504813	240	Volvo	1993	Available	243.68	12	66
74	4363144	Sunfire	Pontiac	1995	Available	439.95	7	214
75	7973598	M-Class	Mercedes-Benz	2001	Available	207.62	12	285
76	1339582	Baja	Subaru	2003	Rented	323.21	9	112
77	5856422	Sable	Mercury	1999	In Maintenance	354.32	5	89
78	5961271	Civic	Honda	2001	In Maintenance	156.27	12	149
79	2323944	90	Audi	1994	Available	278.64	5	201
80	5788595	Defender Ice Edition	Land Rover	2010	Available	173.95	2	56
81	9732584	Transit Connect	Ford	2012	In Maintenance	125.21	4	9
82	5208770	V70	Volvo	2002	Rented	393.54	12	303
83	2841052	S-Class	Mercedes-Benz	2010	Available	371.26	5	100
84	4048419	Z4	BMW	2006	In Maintenance	151.85	12	274
85	6750438	Econoline E150	Ford	1994	Rented	446.61	9	118
86	7058780	Supra	Toyota	1992	In Maintenance	175.56	5	243
87	5088233	8 Series	BMW	1995	Rented	475.16	12	234
88	5460498	Murano	Nissan	2009	In Maintenance	337.54	5	387
89	7801354	Navigator L	Lincoln	2011	In Maintenance	406.00	12	305
90	8039092	Econoline E250	Ford	1999	In Maintenance	160.74	9	315
91	1296313	Pacifica	Chrysler	2008	Rented	167.75	4	59
92	9810171	Sebring	Chrysler	2009	In Maintenance	167.06	9	379
93	6988194	Metro	Chevrolet	2001	Rented	153.55	4	31
94	1320711	MX-5	Mazda	2012	In Maintenance	493.14	4	226
95	8068834	Galant	Mitsubishi	1998	In Maintenance	132.05	4	146
96	1492766	Grand Cherokee	Jeep	2006	Rented	202.82	2	327
97	1809502	Equinox	Chevrolet	2010	Available	392.11	5	117
98	1555793	xB	Scion	2009	Rented	467.08	9	313
99	2115560	Expedition	Ford	1999	In Maintenance	239.37	5	67
100	7543863	Ascender	Isuzu	2003	Available	346.60	12	115
101	3885372	Discovery	Land Rover	2001	Rented	189.28	7	113
102	1166103	LTD	Ford	1985	Rented	424.08	4	102
103	3077896	RDX	Acura	2011	Available	171.34	7	270
104	2306591	Firebird	Pontiac	2002	Available	397.17	9	276
105	2454108	Tiguan	Volkswagen	2011	Available	219.77	2	391
106	5196641	TT	Audi	2004	Rented	199.53	2	76
107	7507933	A4	Audi	2011	Available	221.71	5	244
108	8866747	Stratus	Dodge	2005	Rented	408.71	5	380
109	8819368	Touareg	Volkswagen	2004	Available	454.56	7	248
110	9912914	911	Porsche	1988	Rented	427.37	12	358
111	8883800	Grand Marquis	Mercury	2000	In Maintenance	209.25	2	303
112	9263646	Dakota	Dodge	1995	Available	305.01	7	320
113	9045741	TT	Audi	2002	In Maintenance	409.77	9	46
114	7835226	G	Infiniti	2004	Rented	140.77	9	101
115	5062632	C70	Volvo	2000	In Maintenance	115.47	9	326
116	8268567	Crown Victoria	Ford	2006	Available	484.96	2	132
117	9300512	Camaro	Chevrolet	1995	Available	435.86	5	113
118	8398739	Miata MX-5	Mazda	1994	In Maintenance	352.87	4	288
119	2943134	LS	Lexus	2007	Rented	442.39	12	25
120	6665380	Maxima	Nissan	1997	In Maintenance	384.57	12	171
121	7520036	CLK-Class	Mercedes-Benz	2004	Available	405.36	2	173
122	7863380	Liberty	Jeep	2005	Rented	418.32	2	363
123	1420463	Cougar	Mercury	1996	Rented	442.80	12	177
124	9495990	Sable	Mercury	1998	Available	118.78	9	339
125	5235832	Defender	Land Rover	1994	In Maintenance	401.76	7	176
126	6770392	Tundra	Toyota	2004	In Maintenance	328.32	12	10
127	4458736	Discovery	Land Rover	2002	In Maintenance	294.08	12	77
128	1864247	Q	Infiniti	2002	Rented	343.57	12	196
129	4694038	Discovery	Land Rover	2012	Rented	187.01	2	58
130	3911870	H2	Hummer	2007	Rented	438.60	9	295
131	7391744	Ram	Dodge	2010	Rented	217.50	4	102
132	3148416	Coachbuilder	Buick	1992	In Maintenance	373.85	7	259
133	6327424	E-Series	Ford	2001	In Maintenance	488.16	5	128
134	4583904	400SEL	Mercedes-Benz	1993	In Maintenance	238.32	4	102
135	3322022	Sonoma	GMC	1999	In Maintenance	209.87	2	209
136	2675701	Grand Prix	Pontiac	1988	In Maintenance	441.91	7	167
137	3822191	Tempo	Ford	1992	In Maintenance	397.75	4	349
138	3970225	Probe	Ford	1997	In Maintenance	284.35	7	170
139	2468433	9000	Saab	1998	Rented	136.99	5	65
140	6309897	Odyssey	Honda	2010	In Maintenance	131.32	12	124
141	5035835	9-5	Saab	2001	Available	121.18	7	3
142	9984702	Astro	Chevrolet	2000	Available	433.35	9	290
143	7307604	S-Series	Saturn	1995	Rented	423.02	9	330
144	5023098	PT Cruiser	Chrysler	2006	In Maintenance	308.53	12	202
145	8973940	Excursion	Ford	2003	Available	132.53	12	335
146	6311759	Fleetwood	Cadillac	1992	In Maintenance	340.34	2	309
147	1538687	Montana SV6	Pontiac	2006	Rented	216.59	9	94
148	1089832	Carrera GT	Porsche	2004	Available	191.27	7	184
149	8385858	745	BMW	2003	Available	269.07	9	268
150	7700394	RVR	Mitsubishi	1994	In Maintenance	377.04	2	279
151	8579974	164	Alfa Romeo	1994	Available	196.39	4	187
152	1046642	960	Volvo	1993	Rented	424.78	5	81
153	2106264	Insight	Honda	2002	Available	125.58	5	210
154	1514933	Legacy	Subaru	2000	Rented	199.77	7	171
155	5847773	Tribute	Mazda	2004	In Maintenance	142.47	7	335
156	7550290	Maxima	Nissan	2009	Rented	221.35	4	275
157	5490411	rio	Volkswagen	2001	Available	100.54	12	316
158	6587434	3 Series	BMW	2006	In Maintenance	135.43	2	265
159	6856493	Enclave	Buick	2009	Rented	108.41	5	61
160	6673126	1500	GMC	1995	Rented	197.56	12	247
161	4036965	Thunderbird	Ford	1987	Available	280.42	12	138
162	8675404	E-Class	Mercedes-Benz	2003	Available	148.60	7	78
163	1969626	CTS	Cadillac	2006	Available	484.88	5	261
164	3929154	Avenger	Dodge	1995	In Maintenance	311.17	4	383
165	6996473	F-Series Super Duty	Ford	2011	Available	310.97	9	377
166	8186459	Silverado 3500	Chevrolet	2006	In Maintenance	382.94	12	106
167	5755975	New Yorker	Chrysler	1996	Available	431.15	9	149
168	5726842	MX-5	Mazda	2012	In Maintenance	198.55	2	34
169	3211624	Mark LT	Lincoln	2007	In Maintenance	179.11	2	56
170	5046909	Xterra	Nissan	2003	Rented	202.50	2	46
171	6416684	LHS	Chrysler	1995	In Maintenance	454.67	12	294
172	2047748	F150	Ford	2003	Rented	109.60	5	112
173	4191994	Thunderbird	Ford	1997	In Maintenance	156.23	9	315
174	4101115	Escort	Ford	1999	In Maintenance	150.25	2	397
175	5596181	Sierra 2500	GMC	2002	Rented	274.37	7	294
176	8508131	CR-V	Honda	1999	Available	125.54	4	98
177	4017987	Suburban 1500	Chevrolet	2002	Rented	306.06	2	128
178	3260388	Rodeo	Isuzu	2003	Available	194.24	5	181
179	1036980	Allante	Cadillac	1993	Rented	409.97	12	247
180	5157752	Neon	Dodge	2000	In Maintenance	312.22	4	80
181	7340231	Suburban 2500	Chevrolet	1996	In Maintenance	409.68	2	260
182	1526159	MPV	Mazda	2002	In Maintenance	168.89	9	311
183	1586236	LFA	Lexus	2012	In Maintenance	389.73	5	298
184	7128765	Sierra 1500	GMC	2000	Available	331.87	2	10
185	3947479	D150	Dodge	1993	Available	400.46	7	30
186	1303070	Econoline E350	Ford	2002	Available	163.80	7	298
187	4487385	Nitro	Dodge	2008	Available	339.65	5	198
188	9887594	Viper	Dodge	2006	Available	189.46	12	371
189	8017946	F-Series	Ford	1993	In Maintenance	178.80	12	331
190	9811705	Frontier	Nissan	2005	Rented	166.44	2	150
191	2559528	A6	Audi	2005	In Maintenance	328.49	12	364
192	4170973	F-Series Super Duty	Ford	2012	Available	401.85	5	230
193	4901300	X5	BMW	2004	In Maintenance	149.16	5	11
194	1247934	Passat	Volkswagen	2010	Available	396.45	2	205
195	9622051	Sparrow	Corbin	1999	Available	110.05	9	216
196	7480437	F250	Ford	2005	Available	213.70	2	243
197	5226289	Viper RT/10	Dodge	1993	In Maintenance	293.24	12	258
198	4338804	100	Audi	1991	Rented	253.01	9	110
199	2834484	G37	Infiniti	2010	Available	483.99	9	335
200	3497785	9-5	Saab	2001	Available	143.90	9	146
201	1716712	850	Volvo	1996	Available	391.36	5	189
202	2190052	GS	Lexus	1998	Available	365.62	2	227
203	7650841	ES	Lexus	1989	Available	329.24	5	179
204	9545284	Aerostar	Ford	1989	In Maintenance	267.44	4	119
205	2649316	Viper	Dodge	1998	Available	246.57	9	365
206	4987243	C70	Volvo	2004	Rented	171.85	9	325
207	6784806	Yukon XL 1500	GMC	2009	Available	428.96	12	171
208	8878702	3500	Chevrolet	1995	Available	393.10	2	394
209	2629030	Altima	Nissan	2012	Available	487.16	4	288
210	9321270	Murciélago	Lamborghini	2005	In Maintenance	226.36	9	398
211	8191199	Alcyone SVX	Subaru	1996	Rented	497.48	2	31
212	2456547	Maxima	Nissan	2001	Rented	124.14	2	356
213	2406450	Golf	Volkswagen	1989	Available	106.88	4	270
214	7426911	300ZX	Nissan	1996	Rented	452.98	5	59
215	7997898	Viper	Dodge	2003	In Maintenance	212.52	9	138
216	4925967	GTO	Pontiac	1967	Available	335.57	12	200
217	2120138	Countach	Lamborghini	1985	Available	394.62	5	1
218	4196106	RSX	Acura	2006	In Maintenance	359.32	2	278
219	9035355	Ram Van 3500	Dodge	2001	Available	356.17	4	236
220	1237894	VS Commodore	Holden	1997	Available	189.46	4	230
221	3246907	Sentra	Nissan	2004	Available	252.83	5	351
222	5631324	1 Series	BMW	2008	In Maintenance	128.52	4	93
223	6312829	Murano	Nissan	2005	In Maintenance	360.32	2	184
224	7175292	Defender	Land Rover	1994	In Maintenance	416.59	4	259
225	4564229	Sidekick	Suzuki	1991	Available	402.65	5	137
226	7115866	Savana 3500	GMC	2007	Rented	441.63	9	116
227	3338863	Cougar	Mercury	1992	Available	140.76	9	138
228	2821076	Durango	Dodge	2011	Rented	327.27	12	147
229	4630345	Econoline E350	Ford	2001	Available	126.18	4	346
230	2594850	F350	Ford	2001	Rented	449.85	12	222
231	5007422	Fit	Honda	2008	In Maintenance	304.88	5	196
232	5689173	LS	Lexus	2009	In Maintenance	214.10	5	223
233	7574235	Probe	Ford	1994	In Maintenance	423.42	4	58
234	7147451	Montero Sport	Mitsubishi	2001	In Maintenance	325.89	9	307
235	2562888	Corvette	Chevrolet	1975	In Maintenance	452.75	4	312
236	5824598	Rio	Kia	2008	Available	176.90	9	301
237	2869989	Golf	Volkswagen	2002	Available	266.47	9	94
238	6759567	M3	BMW	1997	Available	105.54	2	238
239	1129623	Savana 2500	GMC	2008	In Maintenance	430.34	12	8
240	1991203	HHR	Chevrolet	2011	In Maintenance	309.63	2	160
241	5442031	Cutlass Supreme	Oldsmobile	1997	In Maintenance	441.25	7	38
242	7389964	Suburban 1500	Chevrolet	2005	In Maintenance	288.19	4	321
243	5927254	Sunfire	Pontiac	2003	Rented	178.17	9	111
244	5254786	Mustang	Ford	1986	Available	251.23	9	270
245	3309774	C8 Laviolette	Spyker	2004	Available	380.92	5	390
246	2206504	Truck	Mitsubishi	1993	Rented	273.79	5	168
247	5428826	S10 Blazer	Chevrolet	1992	Available	426.85	7	138
248	5275051	Grand Marquis	Mercury	1988	Rented	398.65	4	5
249	8384912	525	BMW	2006	Available	292.26	9	348
250	6107255	Achieva	Oldsmobile	1995	In Maintenance	254.02	5	85
251	1181523	Quattroporte	Maserati	2007	Available	152.16	9	318
252	3219710	Camry Solara	Toyota	2008	Available	177.08	4	75
253	2769605	Silverado	Chevrolet	1999	Rented	246.63	5	55
254	5203515	Quest	Nissan	1997	Available	294.15	9	58
255	7845543	Highlander	Toyota	2002	Rented	375.24	5	389
256	4485176	Impreza	Subaru	2007	Available	332.72	2	38
257	7814317	Navigator	Lincoln	2004	Available	449.79	5	295
258	5140235	F250	Ford	1996	Available	282.71	5	129
259	6187348	Cabriolet	Volkswagen	1986	Available	472.39	2	260
260	6964528	Tahoe	Chevrolet	2009	In Maintenance	317.07	5	321
261	7930540	Mustang	Ford	2005	In Maintenance	214.57	4	184
262	2908263	MDX	Acura	2005	Rented	127.98	4	287
263	8233451	Camry	Toyota	1996	In Maintenance	372.20	7	87
264	5478448	MKS	Lincoln	2009	Available	245.00	7	47
265	1128082	Five Hundred	Ford	2006	Rented	388.20	9	277
266	7566171	Matrix	Toyota	2011	In Maintenance	361.37	5	58
267	3794313	Sportvan G30	Chevrolet	1995	Available	274.42	7	38
268	1044097	Accord	Honda	1988	Rented	455.80	5	369
269	4912535	S60	Volvo	2007	Rented	363.04	7	97
270	2764177	S-Class	Mercedes-Benz	2009	In Maintenance	490.53	7	221
271	1729380	QX	Infiniti	1997	In Maintenance	415.72	4	50
272	3514879	LS	Lexus	2003	In Maintenance	323.88	12	20
273	8493954	Ram Van B250	Dodge	1994	Available	185.61	12	51
274	3839928	MKX	Lincoln	2012	Available	384.45	4	384
275	3341651	Genesis Coupe	Hyundai	2011	In Maintenance	199.21	5	162
276	9593985	Highlander	Toyota	2004	Rented	236.47	2	206
277	6010424	Mulsanne	Bentley	2011	Rented	322.24	2	355
278	4571533	CX-9	Mazda	2007	Available	240.94	12	77
279	6170119	Phaeton	Volkswagen	2004	In Maintenance	387.50	2	239
280	9778564	Astro	Chevrolet	2005	Rented	422.82	7	188
281	1518787	Explorer Sport	Ford	2002	In Maintenance	220.62	9	346
282	6161534	I	Infiniti	1998	Available	483.22	4	278
283	3270972	S8	Audi	2003	Rented	405.54	12	81
284	4254491	Aurora	Oldsmobile	2003	In Maintenance	149.22	12	334
285	9107247	Vantage	Aston Martin	2009	In Maintenance	480.98	4	145
286	3021934	SLR McLaren	Mercedes-Benz	2009	Available	107.88	7	167
287	9937540	370Z	Nissan	2012	In Maintenance	182.64	2	101
288	7243896	Interceptor	Jensen	1967	Available	461.58	2	307
289	2555122	Quest	Nissan	2012	Rented	211.64	9	1
290	6709747	Grand Marquis	Mercury	1999	Rented	465.42	12	306
291	9099447	600SEL	Mercedes-Benz	1993	Available	481.57	12	147
292	5504413	Camaro	Chevrolet	1973	Rented	128.75	5	238
293	8233649	Monte Carlo	Chevrolet	1998	Available	394.72	2	215
294	1671552	Thunderbird	Ford	2004	Available	122.17	9	386
295	6427634	164	Alfa Romeo	1993	Rented	103.17	12	336
296	4382981	Pathfinder	Nissan	2012	Rented	462.69	2	372
297	5657395	X3	BMW	2012	In Maintenance	239.20	5	234
298	7026535	Fox	Volkswagen	1989	Available	342.17	9	77
299	5461258	Allroad	Audi	2003	Available	322.05	9	38
300	6938572	Sierra 2500	GMC	2011	Available	227.45	7	271
301	9980478	500SEC	Mercedes-Benz	1993	Rented	322.59	12	222
302	4714812	Ram Wagon B150	Dodge	1994	Available	215.59	9	297
303	1513388	Accord	Honda	1988	Available	222.90	9	188
304	3826049	Aero 8	Morgan	2009	Rented	254.20	12	24
305	5693276	Exige	Lotus	2005	In Maintenance	311.53	12	108
306	3661774	CR-Z	Honda	2012	In Maintenance	247.82	5	198
307	5456375	Pajero	Mitsubishi	1988	Rented	146.28	5	61
308	2101031	Sable	Mercury	1988	Available	374.54	4	218
309	8422981	Corvette	Chevrolet	2012	In Maintenance	230.17	2	14
310	5695955	X3	BMW	2011	Rented	387.12	7	87
311	9456855	Ram Van 2500	Dodge	1997	Available	425.72	5	327
312	7791212	TL	Acura	2009	Available	130.53	5	165
313	7011780	Escalade	Cadillac	2007	Available	405.36	2	329
314	3709906	Sunbird	Pontiac	1991	In Maintenance	361.54	4	65
315	5723104	TT	Audi	2002	In Maintenance	133.72	2	8
316	5321254	Quattroporte	Maserati	2005	Rented	164.40	4	343
317	2644275	Passat	Volkswagen	1996	Rented	115.49	9	41
318	7378868	E350	Ford	2003	Rented	267.01	12	377
319	4144038	Concorde	Chrysler	2000	Available	464.18	2	161
320	8544220	Freelander	Land Rover	2004	Available	288.36	12	369
321	2941413	Silverado 1500	Chevrolet	2005	Available	467.28	5	155
322	3003811	Outlook	Saturn	2007	Available	477.81	4	323
323	6763060	Intrigue	Oldsmobile	2002	Rented	268.17	4	215
324	6513015	Grand Vitara	Suzuki	2002	In Maintenance	363.78	5	97
325	4752326	Tiguan	Volkswagen	2012	Available	495.01	12	86
326	7961205	Daewoo Lacetti	Suzuki	2007	Rented	100.71	12	6
327	2472207	FX	Infiniti	2008	In Maintenance	247.83	4	272
328	1512083	Avenger	Dodge	2008	In Maintenance	232.72	4	274
329	3258388	928	Porsche	1995	Available	387.60	7	201
330	9032677	Odyssey	Honda	2003	Rented	449.76	2	9
331	5366521	9-3	Saab	2000	Available	224.55	5	212
332	4613243	Sonoma Club Coupe	GMC	1996	In Maintenance	333.82	5	341
333	9825281	Grand Prix	Pontiac	1962	Available	400.40	4	324
334	5377597	Crown Victoria	Ford	2011	In Maintenance	483.47	5	281
335	3487462	Focus	Ford	2012	Rented	483.48	9	126
336	3700718	Vandura 3500	GMC	1994	In Maintenance	390.56	7	391
337	9573237	Celica	Toyota	1992	Rented	104.00	4	380
338	3912929	Explorer	Ford	2012	In Maintenance	196.57	4	124
339	1957731	Savana 1500	GMC	1999	Available	203.20	2	133
340	9198177	Continental	Lincoln	1990	In Maintenance	318.75	9	346
341	4323707	LaCrosse	Buick	2005	Rented	154.46	12	340
342	5457971	Bronco	Ford	1993	Rented	299.92	2	56
343	5496378	2500	Ram	2011	Available	476.13	9	12
344	1213688	STS	Cadillac	2008	In Maintenance	450.22	12	21
345	8627092	Santa Fe	Hyundai	2003	Rented	270.93	4	123
346	6887824	Elise	Lotus	2005	In Maintenance	250.36	4	301
347	1085579	SL-Class	Mercedes-Benz	2005	In Maintenance	479.56	4	144
348	4354952	Coupe Quattro	Audi	1991	In Maintenance	305.20	12	96
349	3532982	Challenger	Mitsubishi	1998	In Maintenance	281.31	7	70
350	1542767	QX56	Infiniti	2007	In Maintenance	186.06	5	205
351	7534472	Tracer	Mercury	1997	In Maintenance	417.65	12	91
352	2709648	Bravada	Oldsmobile	1997	In Maintenance	129.93	12	264
353	9986680	Concorde	Chrysler	2004	Rented	426.74	2	242
354	5077860	Tiguan	Volkswagen	2009	In Maintenance	319.76	5	124
355	3882530	LeMans	Pontiac	1966	In Maintenance	267.85	9	150
356	7247372	Daewoo Lacetti	Suzuki	2008	In Maintenance	134.27	4	148
357	4723952	Accord	Honda	1984	In Maintenance	471.32	12	253
358	6571216	VehiCROSS	Isuzu	2001	In Maintenance	138.73	2	89
359	2520863	Celica	Toyota	1992	In Maintenance	374.39	12	260
360	1848252	57	Maybach	2012	Available	499.43	12	97
361	3143939	Sonata	Hyundai	2002	Available	375.03	5	396
362	8119367	Regal	Buick	1998	Rented	156.24	7	143
363	8519634	Familia	Mazda	1986	In Maintenance	453.90	2	83
364	5183297	Type 2	Volkswagen	1987	In Maintenance	318.95	12	304
365	8311692	CT	Lexus	2011	Rented	283.65	9	114
366	2960738	Sprinter	Dodge	2009	Rented	495.32	2	275
367	8759479	Tacoma	Toyota	1996	In Maintenance	393.36	12	262
368	1728276	Chariot	Mitsubishi	1986	In Maintenance	383.27	9	294
369	3159174	Golf	Volkswagen	1986	Available	159.16	7	208
370	3761260	Fox	Volkswagen	1988	Rented	336.60	12	222
371	4789833	3000GT	Mitsubishi	1992	Rented	463.96	12	236
372	3502545	57	Maybach	2003	In Maintenance	260.75	12	232
373	7332106	Prius	Toyota	2001	Available	231.02	9	381
374	6359500	B9 Tribeca	Subaru	2007	Available	471.29	2	353
375	2872377	Cabriolet	Volkswagen	2001	Rented	492.11	12	397
376	5837361	Landaulet	Maybach	2011	Available	166.02	4	139
377	4287954	9000	Saab	1994	In Maintenance	153.61	4	352
378	4267479	Grand Marquis	Mercury	1997	In Maintenance	376.53	9	16
379	7730872	3 Series	BMW	1996	Rented	278.75	7	272
380	4876471	Envoy XL	GMC	2003	Rented	252.96	4	4
381	6959192	Ram 2500	Dodge	1996	Available	446.26	7	309
382	4205377	CLK-Class	Mercedes-Benz	2006	Available	253.53	12	231
383	1659164	Sienna	Toyota	2004	Available	125.06	12	83
384	3055771	Biturbo	Maserati	1987	Rented	486.40	4	351
385	2473035	Impala	Chevrolet	2003	Available	420.35	2	54
386	7801005	Sienna	Toyota	2002	In Maintenance	251.95	5	207
387	8201531	S-Type	Jaguar	2008	Rented	232.61	2	299
388	2654899	Grand Voyager	Chrysler	2000	Available	329.97	2	132
389	7578102	200	Chrysler	2012	Available	193.77	9	304
390	9508174	Tundra	Toyota	2011	Available	104.35	7	322
391	6513161	Freestyle	Ford	2007	Available	336.11	9	366
392	5998942	Explorer	Ford	1994	In Maintenance	104.86	9	1
393	4746795	G8	Pontiac	2009	Rented	345.59	5	236
394	4928875	S-Class	Mercedes-Benz	2011	Rented	348.71	5	187
395	2023574	Grand Cherokee	Jeep	1995	Available	459.37	5	28
396	6608261	Elise	Lotus	2004	In Maintenance	336.33	2	17
397	3984198	Viper	Dodge	2009	Available	369.69	5	165
398	5991568	TL	Acura	2006	Rented	389.89	4	330
399	2561177	EX	Infiniti	2010	In Maintenance	266.39	9	300
400	5533708	XJ Series	Jaguar	2001	Available	103.64	5	334
401	4558358	Ram Van 2500	Dodge	2003	Rented	486.00	12	373
402	1237389	Pilot	Honda	2004	In Maintenance	474.57	2	247
403	5485967	J	Infiniti	1994	In Maintenance	171.45	5	11
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: shira
--

COPY public.customer (customerid, firstname, lastname, phone, email, licensenumber, dateofbirth) FROM stdin;
4	מוחמד	בוחבוט	0590689552	pshvrts@example.org	9215058	1988-01-18
5	יעל	חמו	0591792515	rpl00@example.com	5997987	2001-07-23
6	נעמה	טויטו	080473773	tbrhmy@example.org	2469686	1979-06-08
7	מוסטפא	איפרגן	082333553	lyb56@example.com	2043678	1990-07-14
8	דניאל	בדראן	021105557	kmmn@example.org	4444878	1960-10-19
9	יאיר	כהן	049520626	dykhn@example.org	5594081	1991-07-13
10	גיא	רוזנטל	0577233889	dryyvsp@example.com	5819357	1968-04-03
11	הילה	אביטל	0562160296	vzsd@example.net	9124377	1958-05-02
12	אורין	ספיר	097405337	itvytv@example.com	3672869	1968-06-04
13	רחל	טל	044482734	yvlshmvn@example.com	8541399	1964-12-29
14	אלון	ניר	099171995	yhvntn99@example.com	4576592	1961-03-15
15	איתי	רובין	0584361042	ymynshlv@example.net	4653591	1977-07-21
16	משה	רבינוביץ	085386967	zvkhyvn@example.com	9061219	1955-05-05
17	תמר	עזרא	047999426	hlllynh@example.org	7970718	1955-11-21
18	אחמד	אביטבול	024177096	dn41@example.net	2300778	1965-06-03
19	איילה	פרץ	0508075923	shyrhlys@example.com	7484570	1964-08-17
20	שקד	כהן	099487002	ovvlp@example.org	3473218	1999-07-15
21	אוריה	אבו אל היג'א	043538809	dl73@example.net	4723040	1966-03-26
22	אליה	דאוד	026366981	myryhvntn@example.com	5623545	2005-10-28
23	גוד	כהן	0540513203	mshhshkhdh@example.org	6835697	1989-02-13
24	משה	שאהין	033971734	shyr12@example.org	4594170	1952-08-02
25	ג'ורי	אלוש	037982628	ny39@example.com	5331117	2001-11-08
26	נעמה	אלטורי	0535615645	lmrbdrnh@example.net	2984947	1960-02-20
27	רבקה	מנסור	093381051	gl14@example.com	7088544	1976-06-27
28	רוני	ספיר	026262215	fbrmn@example.com	9111508	1997-05-01
29	יוסף	פרץ	0524151195	nghzydn@example.com	8777536	1953-11-26
30	אליהו	לוי	0500968438	khnshrh@example.com	1241797	1966-01-23
31	עדי	כץ	085295267	pkhdd@example.com	2478974	1954-11-23
32	ליבי	רזניק	0561359282	brhmytn@example.net	6864190	1960-07-30
33	מוחמד	גולן	036006856	glyhnyr@example.com	2558534	1954-05-29
34	אמיליה	סלאמה	0588411129	yhvdyt03@example.com	3471570	1968-04-13
35	שרבל	יעקובוביץ	0595267701	ytymsry@example.net	6016685	1988-03-09
36	אביאל	נעים	0529979167	bygylmsry@example.net	1933185	1988-05-09
37	ענבר	לוי	088523639	shkhdhmvstp@example.org	2979677	1986-03-22
38	אביה	מרדכי	084318723	egnym@example.net	5552724	2001-03-02
39	יולי	ג'בארין	087148697	yqyr58@example.net	6104663	1973-04-20
40	אבראהים	שושן	028559823	bdrnhhdr@example.org	5575178	2003-04-22
41	עומר	אזולאי	020987400	brhm93@example.net	5519622	1991-10-27
42	שהד	חביבאללה	026152621	ytn85@example.com	1473305	1963-03-28
43	חיה	שוורץ	027114073	jdql@example.com	1698827	1990-07-18
44	אדל	רז	0590129316	mrym02@example.net	1889595	1954-10-08
45	מוחמד	דהן	040271084	xgl@example.net	7115649	1985-01-22
46	דוד	אוחיון	087982496	yhly34@example.org	6896757	1965-06-03
47	רבקה	עאמר	089801241	bt-shb08@example.com	6191417	1974-04-11
48	נאור	גנאים	0539358327	myklbd-l-qdr@example.com	6065902	1970-08-28
49	אסתר	חמוד	045276576	zynb11@example.com	3496382	1985-09-16
50	אלה	לוי	048038030	vz60@example.net	3843664	1979-05-24
51	עובדיה	יצחק	045813259	khlylhrvmy@example.com	3385653	1959-12-28
52	אורי	אורן	0590603012	brmvbrd@example.org	5930875	2007-02-08
53	ליאן	פז	0528361394	yskhvqnyn@example.org	8982890	1958-01-23
54	ליה	איסקוב	097072045	yshymdr@example.net	3394834	1954-11-17
55	נויה	כהן	0583560249	mrymlqvby@example.net	6540650	1952-05-10
56	יהונתן	כהן	0565363490	gpn45@example.org	7330294	1959-09-18
57	ג'נא	חיים	0536241891	rlykmh@example.org	3930581	1974-11-30
58	שאם	סויסה	095775223	shrvnylyn@example.org	9633162	1992-11-28
59	מיכאל	קפלן	041133982	rvbnlyvr@example.com	7306636	1985-10-22
60	כרמל	כהן	081135049	qlby@example.org	2882772	1964-02-03
61	דביר	אוזן	040612156	rpl82@example.com	4107078	2000-05-28
62	טובה	אבני	081606095	bytl42@example.com	4568140	1968-02-02
63	אלין	לוי	089923779	dvd25@example.net	4863402	1999-08-24
64	יהלי	חן	024600371	dvdyvbl@example.net	4044410	1968-12-07
65	נגה	אהרן	037718285	bnymynshlvm@example.net	7231875	1987-01-12
66	שמעון	מימון	099795213	rvykhvry@example.net	7160080	1971-02-27
67	תמר	כהן	021082067	ikhyvn@example.com	9259877	1981-02-07
68	משה	כהנא	0575651562	slymnndb@example.net	9902528	1996-03-07
69	יאיר	כהן	027426376	zvhr10@example.com	9114424	1962-01-24
70	אלישע	הראל	084162442	ydydyhlvy@example.net	7288871	1960-08-19
71	בלומה	כהן	092563635	drvrbn-shbt@example.com	6482748	1954-12-21
72	רוי	לוי	082143098	ytylb@example.org	9458978	1998-03-27
73	דניאלה	כהן	0548890085	mbdyr@example.net	7674675	1990-07-30
74	יהלי	עודה	027196893	rvm94@example.net	2962780	1995-07-22
75	חיים	מיכאלי	037237614	gvly56@example.com	4968675	1991-12-28
76	רוני	סבג	081743827	khyymvbbrhm@example.net	7186016	1987-04-30
77	מיכאל	אוחיון	0569869140	vmzrkhy@example.net	6453385	1970-07-01
78	יעל	גרין	0572892942	zynh92@example.net	9172186	1962-03-14
79	יעקב	קאסם	091983597	dl48@example.com	7735793	1995-06-23
80	נעמי	נחום	026516678	nykhmv@example.org	3607813	1978-08-05
81	עידו	אשכנזי	099016591	lyvrdvytsh@example.net	9743111	1956-12-18
82	רומי	סבאג	080925111	yvblybvbyts@example.com	9943544	1988-05-10
83	בתיה	גרוסמן	0501306131	shrhgrvs@example.com	9247779	1982-05-18
84	שקד	שמעוני	021228521	yhlydql@example.com	4775511	2002-12-09
85	יהונתן	ויצמן	024604971	nvhkhn@example.net	1938439	1958-04-12
86	הדר	לב	049023733	brqvbytsmy@example.org	2252855	1953-08-21
87	שמעון	אלסייד	040847529	nhvrbyts@example.net	5550942	1962-11-05
88	יהונתן	כהן	022853254	nslkh@example.net	2267068	1968-03-03
89	עבד	בן הרוש	022075891	rmkhgnh@example.net	6238237	1964-09-03
90	בניה	יחזקאל	032113828	lh87@example.org	3398671	1952-01-03
91	ניקול	פחימה	081216012	mrym48@example.com	7388497	1977-11-28
92	אביחי	בקר	0520831775	lvynlyrz@example.com	4162248	1993-08-27
93	מלכה	עוזרי	038258502	prydmnyty@example.com	3736992	1986-02-26
94	רוני	לוי	095743476	tlyh36@example.com	6324098	1976-03-27
95	רים	טייב	086925918	uyprkh@example.com	4090366	1992-12-30
96	חוה	עמית	086158088	pprydmn@example.org	4333709	1975-05-30
97	יהונתן	בשיר	0562558911	shgb31@example.org	9511475	2005-09-14
98	ישראל	סיני	0594272824	khznmvs@example.net	7254203	1983-08-04
99	דן	רוזנטל	099285627	vkhn@example.net	5124515	2005-08-29
100	חיה	כחלון	087609362	hrrykhvsyn@example.org	2379495	1998-09-26
101	שמואל	שלום	021346608	yhl48@example.org	2281629	2001-05-15
102	נועה	אזולאי	031463664	nmymlvl@example.org	5055138	1970-09-13
103	מאיה	מלכה	0569111192	khmd75@example.org	8914821	1968-09-12
104	חסן	אלקיים	034767234	prymkhmvd@example.com	5115752	1960-03-19
105	מוחמד	חי	0559633394	yylh69@example.org	1607430	2000-01-11
106	משה	אברגל	041108427	mmr@example.com	2617873	1995-12-02
107	גאיה	כהן	0581954520	yzvly@example.org	5540565	1957-12-27
108	איילה	חסן	085885306	ksvpr@example.com	8559249	1951-03-27
109	גלי	הירש	0545459388	khmd44@example.org	6499295	1951-09-11
110	שאם	חי	044967122	bygyl63@example.com	9866976	1970-10-28
111	מחמוד	מימון	046876096	mly92@example.net	8301781	1976-09-18
112	מוחמד	לוי	097269432	nvprkhn@example.org	3043916	1974-10-13
113	עדי	אנגל	049697862	gmnsvr@example.org	4663056	1986-08-17
114	ינון	כץ	044762299	shyrhlbz@example.com	6548777	1962-02-19
115	עלי	כהן	040895911	brkhvkhyvn@example.com	8519435	1950-11-06
116	שי	מזרחי	044162807	brhym66@example.org	6606566	1983-04-16
117	מיאר	דהן	0505834361	pldyl@example.org	9431735	1957-10-16
118	מיכאל	בן חמו	026145823	lys11@example.com	3634270	1979-12-09
119	מאיה	אזולאי	093003787	rz95@example.net	8899683	2003-10-08
120	נעמי	ברקוביץ	0554657478	tmr62@example.org	2774803	1967-06-09
121	הלל	אליהו	032661802	hvdyhsbg@example.org	1172644	1990-08-22
122	מנחם	שחר	0508335680	pyshrlh@example.org	3611641	1971-09-22
123	איתמר	נסאר	027906171	dvdlyrz@example.net	8419100	1985-04-18
124	אלמא	גיל	089462950	vrshvbl@example.net	6410815	1995-02-18
125	אוריאן	שביט	029789254	hyybmvkhmd@example.org	7791636	1973-02-09
126	עלמה	קמחי	031990375	spyr89@example.com	6050475	1984-03-27
127	עבד	מימון	042332599	hlqrynvy@example.net	6292998	1985-02-11
128	בועז	לוין	0545891446	yhlylys@example.org	3835555	1970-05-25
129	איתי	גוטמן	0546314669	bshrhmvkhmd@example.org	7984220	1990-05-20
130	יעל	טאהא	025964134	mryzvby@example.net	7813513	1953-06-19
131	סיני	מנצור	080471932	lytlkhlylh@example.com	9732746	2003-10-09
132	אורין	אליהו	029952494	mvryshtryt@example.net	6607379	1992-04-25
133	יהודה	פינקלשטיין	047257796	lyh80@example.com	6710703	1972-12-22
134	ג'ורי	יונס	039813193	shmvn04@example.org	9452701	1958-07-20
135	צביה	אלמלח	090613737	mylybrhmy@example.net	3565291	1993-02-01
136	הראל	אוחיון	0541693692	thlvy@example.org	2313650	1951-08-13
137	יעקב	ליבוביץ	044900103	emkhgnh@example.com	6182593	1974-06-20
138	יוסף	ברוך	0540389457	myh19@example.org	5341860	1957-04-21
139	מעיין	גדיר	020729706	ykhy48@example.org	9980833	1959-05-03
140	שירה	פרנקל	030202399	imyr@example.org	4495430	1952-12-14
141	ניסים	טאהא	035441179	svrn@example.net	5759745	1969-10-08
142	יונתן	לוי	021368821	yvntnprts@example.org	8225249	1961-11-13
143	עדן	מזרחי	081239050	khldry@example.net	5223518	1988-01-12
144	אוריאל	ברוך	092193615	osdy@example.org	7855194	1978-01-04
145	נויה	נעים	0571286150	mrdkymntsvr@example.org	7596408	1994-01-06
146	נגה	שפירא	087708646	fprts@example.com	9183305	1969-02-08
147	אדל	גוטמן	0536712378	byshydrvry@example.net	6865985	1983-09-07
148	ארבל	כהן	0550784589	gbrhm@example.net	6435415	2006-02-19
149	רפאל	לוי	0575695627	lytskhqy@example.org	2413519	2006-11-11
150	תמר	רונן	0549313639	dvdgbryh@example.com	9365996	1998-12-17
151	זואי	לוי	095441398	jkhn@example.com	8424255	1951-03-17
152	טליה	ארביב	0587829575	shmvl04@example.org	9368055	1955-02-16
153	עופרי	מילר	0508355742	dnylqlyyn@example.net	2485090	1971-03-15
154	אורין	רוזן	034379589	isbg@example.org	8203410	1956-03-05
155	שגיא	מזרחי	0580195374	thylhvkhnh@example.com	3128515	1985-09-21
156	עילאי	לביא	031498681	dprydmn@example.com	7954213	1988-04-01
157	ליה	אברהם	030246275	tlyhpyntv@example.net	6883863	1996-09-30
158	נעמי	ג'בארין	048273866	khnyly@example.net	4856817	1999-04-04
159	אוריה	וינר	0574424514	khnlvn@example.net	3713390	1959-08-04
160	אימרי	זועבי	089243739	bsyyty@example.net	6616250	1958-11-05
161	לאה	בדר	039396905	kshmvl@example.com	6297037	1997-06-30
162	יובל	גרין	0556110889	ndbsdy@example.org	2163965	1987-07-07
163	טל	מחאמיד	030858373	rvznpldlyby@example.net	2119283	1994-11-01
164	שאם	קורן	039701812	mykl74@example.org	3799760	1955-11-25
165	חוסין	לוי	021052187	mrymlvn@example.net	4365906	1983-01-15
166	עומרי	אופיר	024250009	lyhnkhvm@example.com	4594710	1965-08-27
167	דבורה	פרץ	027280940	mshrvn@example.org	5605370	1994-02-09
168	רות	לביא	088907970	nvyhshvvyqy@example.com	5181471	1949-05-24
169	רועי	ממן	0584910325	rvzntlykhzql@example.com	7894508	1952-06-08
170	יהונתן	אילוז	037501749	lyhvmkhgnh@example.org	6990228	1986-03-12
171	רהף	יחזקאל	0532924253	drvshhmvkhmd@example.org	1205207	1997-12-24
172	איליי	ישראלי	0559135927	bytvnshvn@example.net	6330145	1987-08-01
173	שמואל	קליין	083578339	pshmvn@example.org	9698947	1970-04-21
174	מוחמד	דורון	020539253	pvglmvkhmd@example.com	5476095	2000-12-17
175	אדל	נחום	037889330	brvyys@example.net	5676486	1993-08-22
176	ינון	אלטורי	082416456	lyhykhy@example.org	3742198	1981-07-05
177	נועה	סגל	0503584329	grynbrglyn@example.net	7249586	1960-08-18
178	נועה	עובדיה	0599879406	yldvd@example.com	4162445	1967-08-14
179	אלון	אזולאי	098320983	mvryhmyrh@example.net	9748037	1975-07-25
180	הילי	בראון	086707833	hrl20@example.org	5106275	1971-09-12
181	משה	שוורץ	047217470	lyhvmyr@example.com	1433716	1993-08-31
182	מוחמד	גבאי	0524566984	myrmkhmyd@example.org	5264598	1962-03-26
183	איטה	מאיר	0564554202	hzhby@example.org	1712268	1955-03-22
184	גאיה	שושן	0525702435	rym12@example.com	4754433	1951-12-10
185	מייה	בר	027448932	ntkhn@example.org	2982414	1953-01-24
186	אבישי	מזרחי	0578293869	bvsqylhtlyh@example.net	1138063	1981-10-18
187	תולין	גדיר	020825599	shy-lygvrn@example.net	6139806	1982-11-16
188	אורי	לוי	0514998677	rpllyhv@example.net	1048238	1959-06-01
189	משה	ברוך	043859948	vkhyymvb@example.org	5651864	1972-03-11
190	הראל	בן שבת	028693577	ktsyvsp@example.org	6151952	1959-05-14
191	בניה	מזרחי	029198561	ylhbrqvbyts@example.com	4834680	1998-04-20
192	אורה	נחמני	0546726526	rvny47@example.net	9561058	1987-10-30
193	נעמי	חן	088882691	dvdtyyb@example.org	1066615	1993-11-03
194	ליאן	הלל	0569054353	lyrvy07@example.net	2710045	1967-07-17
195	אביה	יעקובי	083605051	lhdry@example.com	3220853	1960-03-24
196	עידו	כהן	086964825	mrym55@example.com	8713820	1973-07-07
197	ארי	טייב	025508070	lmhpyntv@example.net	6657937	1983-08-12
198	אביגיל	לוי	0555673509	shdhyylh@example.org	7714011	1970-10-04
199	אביאל	כהן	029952772	ylyshshvn@example.org	7953788	1985-08-13
200	נועה	עמר	091616916	mymvnzyyn@example.net	8096263	1988-08-01
201	הילי	חלבי	025894428	zmthl@example.com	1465171	1978-06-19
202	בן	דוד	030422668	yshy93@example.org	9342998	1989-10-31
203	בתיה	שרף	0513107022	bybyvsp@example.org	4298777	1992-10-12
204	גורי	אברמוביץ	046710981	ulrnr@example.net	8121432	1981-08-21
205	נועה	מלול	0529205823	drynvr@example.org	9218177	2001-10-01
206	שני	בן חמו	0533520599	byshg85@example.org	9021077	1966-12-10
207	יהלי	ח'טיב	020818615	rvmybn-shvshn@example.org	1807919	1964-01-05
208	רננה	פוקס	097650826	bryl@example.org	7893251	1956-05-15
209	שני	כץ	0536865445	yvsp03@example.com	3744725	1959-08-05
210	מאיר	דהן	0577424676	glybtsll@example.net	7820628	1974-06-30
211	אמה	נגר	049585176	lyvrh74@example.org	9686920	1990-04-02
212	ליאור	דוד	081370186	yylhmrqvbyts@example.net	4571680	1987-02-15
213	תמר	חדד	049255075	dymkhdd@example.net	6116498	1967-03-03
214	ליאו	כהן	0506210130	hllybrhm@example.com	7529444	1986-05-17
215	עופרי	ברק	0502274565	bnyhgvr@example.net	8104948	1961-10-13
216	אדר	מלכה	038778818	hrl68@example.com	6714584	1958-01-24
217	אלה	סגל	087049474	dn70@example.org	3532430	1998-05-29
218	נועה	ווקנין	0529536525	yl78@example.org	6100709	1958-11-28
219	גיא	ברק	036258960	mnkhm17@example.com	4220127	1999-09-27
220	נועם	סעד	0529653065	nlbvzglv@example.com	6533083	1972-04-25
221	יונתן	אברהמי	0550796599	gkhn@example.org	7749120	2004-08-23
222	אלין	יפת	091394525	nmvrd@example.com	6316737	1997-07-30
223	איתן	מחאמיד	0581712210	bygylkhn@example.org	7869647	1987-06-19
224	גוד	עטיה	0505012171	evvdh@example.net	1915369	1974-04-23
225	הדס	סעדה	043732995	qyshrly@example.net	2442521	1980-03-02
226	איילה	פישמן	048063151	yshrltrsh@example.net	2399427	1991-02-13
227	רואי	דיאב	027717917	bdllhlyrvy@example.net	1418005	1965-02-03
228	בנימין	חדד	025268786	dmbrkh@example.org	5712816	1964-04-27
229	מוחמד	אסדי	040010888	gvlntlyh@example.org	1472121	1992-03-19
230	ליטל	כהן	0525324982	rvkhmh66@example.com	5287681	1999-02-15
231	שירה	ראובן	034214026	yshmvl@example.com	1098280	1993-12-26
232	מילה	מזרחי	089543140	rkhlshytryt@example.com	7647298	1955-06-25
233	איליי	אברהם	042141256	ngh64@example.net	7472511	2003-07-20
234	אופיר	כץ	0523716680	khsn03@example.org	2043669	1970-09-06
235	יוסף	קדוש	0508011699	khngyly@example.com	9427080	1963-06-28
236	אמיתי	אוחיון	031422045	rkhmymyhvsh@example.com	3952501	1977-09-02
237	שמואל	אלוני	037943258	yqb09@example.org	4415448	1976-02-25
238	מאיה	יעקובי	096142357	ytskhqzbrgh@example.com	5715290	1959-03-03
239	רפאל	שפירא	038870074	rvny92@example.net	2358021	1968-08-26
240	שילת	דגן	037886853	brvkvryn@example.com	9415063	1995-02-20
241	אליה	אמסלם	098950513	vmrmkhmyd@example.net	9954639	1978-01-21
242	בניה	נגר	094513353	nmr@example.net	8934345	1984-08-05
243	שי	סבח	049082105	nvhvpyr@example.com	7328613	2003-02-16
244	אדל	חוג'יראת	037254013	usvysh@example.com	5464465	1949-04-01
245	מחמוד	כהן	096379088	rkhl95@example.org	5580497	1977-01-27
246	תומר	ג'בארין	020682265	lyhvytmr@example.com	8250669	1985-12-05
247	יואל	ביטון	0514877567	nvyhshgb@example.net	9539112	1956-12-07
248	יששכר	שושן	0509466740	mkhmvdsymh@example.com	3394456	1990-08-02
249	טליה	חטיב	042468929	prtslyrvy@example.net	1572632	1963-12-19
250	עבד	עזרן	038542988	mrymgvtmn@example.net	7654238	1956-07-27
251	זיין	שכטר	046764372	ybdrn@example.net	8778154	2003-10-26
252	יהודה	זמיר	0594237559	rtvytv@example.com	7346466	2005-05-15
253	גאיה	פרידמן	0566683195	smmn@example.net	2364470	2002-09-07
254	רועי	בן חיים	034204753	lyby39@example.com	7780814	1973-03-10
255	יעקב	צמח	0511095921	tlyn21@example.net	8096948	1957-08-09
256	נועה	ששון	0503154139	ddvydvb@example.com	7667742	1982-05-07
257	אגם	מנחם	0533163153	lynhgbryn@example.com	6160102	1982-02-21
258	אברהם	ברק	0559454109	khyymlvnh@example.com	1274119	1949-10-06
259	נהוראי	גולדשטיין	0524335177	tspvrh68@example.com	4271425	1986-08-10
260	כרים	קאסם	021600467	tmr81@example.com	4445573	1963-12-28
261	שאם	טויטו	034669929	pzvly@example.com	6639568	1958-08-31
262	הראל	שני	0597046981	zbrghmvkhmd@example.com	7446829	1981-11-09
263	רז	אביב	091730715	shmvnshnyydr@example.org	4576012	1987-03-08
264	גיא	ימין	0598089956	bkhgzy@example.net	6504277	1974-01-20
265	איתי	חדד	0564210304	iytskhq@example.org	9929868	1993-12-16
266	אחמד	בר	024373193	gvldh41@example.org	1509599	1993-08-29
267	מוחמד	אבו ליל	0545758073	tvmkhn@example.net	5073116	1975-09-05
268	חיה	מזרחי	0548469789	yhvsh32@example.net	8269846	1979-06-08
269	מיכל	דראושה	039500166	tsvrlyn@example.org	1815527	1957-12-21
270	אביאל	אלוש	0570088795	vhdr@example.com	4584928	2001-10-30
271	אסתר	ברזילי	0516938092	ekhdd@example.net	6304464	1977-09-18
272	אלחנן	פישר	038450545	khyym90@example.com	7684610	1950-05-06
273	יותם	דמרי	025864094	lnyrgb@example.net	1660868	1978-06-10
274	מוריה	דיין	0531545394	rny92@example.org	6250764	1957-12-05
275	ינאי	שרביט	025972176	mvkhmdsgl@example.org	5073556	1993-10-11
276	גולדה	אביטל	039538026	iqvpmn@example.net	2362437	1996-02-04
277	דניאל	מרעי	0578382324	brglytn@example.net	3572596	2001-07-03
278	יוסף	גולדמן	0507786761	rpl28@example.org	9073502	2003-06-05
279	מרים	כהן	044952736	mlmtr@example.com	7358431	1964-02-16
280	רומי	בן דוד	026312632	ekhn@example.com	2748017	1963-04-20
281	רימאס	מזרחי	0518065514	ikhn@example.net	7135355	1968-09-08
282	נעמי	פינטו	049985191	wbrkh@example.net	6086962	1990-09-04
283	משה	טויטו	039263892	nlqrynvy@example.com	3661905	1982-08-16
284	מלאק	מזרחי	025126662	bnymyn92@example.com	4907480	2000-06-11
285	יוסף	עלי	0576647738	dyln64@example.net	1994081	1972-07-05
286	מוחמד	אזולאי	0594900946	nkhmnshrvn@example.com	6742929	1985-10-18
287	אהרון	הרשקוביץ	083725166	ybrqvbyts@example.com	4363154	1989-03-13
288	רומי	שלו	0510849994	yshrlydvd@example.org	7266404	1968-06-25
289	אפרת	שפר	032626084	lmhnsr@example.net	1515932	1955-09-13
290	שחר	מוסקוביץ	026900574	bn61@example.org	8575572	1985-06-30
291	רבקה	קפלן	090367633	fkhn@example.org	7687678	1970-11-30
292	נעמי	אמסלם	0534314043	myprkh@example.com	3651477	1980-07-13
293	נאי	שוויקי	082246065	gkhn@example.com	3524976	1971-04-19
294	אדל	לב	0567889264	yphmyyn@example.org	6673327	1991-05-15
295	אהרון	תורגמן	0515765465	shy-ly50@example.com	2031348	2002-09-03
296	גאיה	מוסקוביץ	0529694937	dnyl91@example.org	3935553	1954-06-21
297	איילה	כהן	048939435	shvrtsyyr@example.com	3576961	1971-06-10
298	עבד	כהן	028445616	vdl66@example.net	9028901	1992-12-15
299	גאיה	עאזם	099916082	shpyrmvkhmd@example.org	4886977	1961-03-16
300	נויה	אהרון	093489419	khnh38@example.org	8839084	1981-04-04
301	עילי	כהן	0552442791	gmlyldvd@example.com	7367664	1999-01-21
302	יעל	בר	0536080131	hrvn77@example.com	8941717	1981-10-01
303	אלעד	טאהא	097301915	qlvy@example.org	8381112	2003-09-29
304	יוסף	ברוך	088146033	yvb82@example.org	2869844	1992-11-08
305	לין	רגב	042243315	gylylsyyd@example.net	2646004	1970-09-13
306	אופיר	גלעד	081350128	ytmr58@example.org	5983148	1998-06-02
307	חיים	פרידמן	031785461	yvnslvn@example.net	6971971	1962-03-10
308	עמנואל	חדאד	0503619056	vlvn@example.org	2599922	1984-03-25
309	אמונה	דדון	031276550	phyrsh@example.net	5050015	2006-01-21
310	לביא	ישראל	0516223558	myly28@example.com	5077882	2002-03-26
311	טוהר	גרוס	044409866	hrvnrvny@example.net	2582230	2003-09-03
312	בנימין	עומר	0515202570	dvd15@example.org	7242117	1979-06-23
313	משה	לוי	0506092420	yhly04@example.com	6093046	1970-08-04
314	שירה	גורדון	0531255669	agnym@example.com	3961312	1985-04-01
315	מאיה	מלול	024336155	yhvntnbytvn@example.org	8011948	1952-09-11
316	אסתר	גרוס	0502334050	lvnkhtyb@example.com	3959031	1990-02-08
317	מאיה	פלד	038129158	lhgvtlyb@example.com	5521100	1957-07-28
318	אור	כהן	0570256237	bnymyngbr@example.com	1170602	1999-07-14
319	תמר	מטר	082668893	rvy43@example.org	9037833	1987-12-21
320	ישראל	מחאמיד	094264147	syqvbvb@example.com	2580336	1999-12-19
321	רפאל	סבג	0567584942	shmvn26@example.net	5471826	1992-04-05
322	עלמה	מטר	0551238984	brhmmvkhmd@example.net	3548393	1989-08-17
323	אייל	לוי	044437685	ysynsd@example.org	5222877	1960-06-05
324	נעמה	מרדכי	039493962	rvt51@example.org	3278149	1961-07-02
325	אביתר	מחאג'נה	038533980	lsymn-tvb@example.com	5253563	1996-11-04
326	נועה	גורן	086971744	tylvz@example.net	9112769	1961-08-15
327	גאיה	רז	0505238776	mvryh87@example.net	7247547	1952-09-04
328	יונתן	גולדשטיין	0532415340	byshg17@example.org	5811108	1959-01-23
329	יסמין	רביבו	0566915268	eshshvn@example.com	1351394	2004-04-14
330	שירה	בצלאל	0568656874	yhvdytly@example.com	6623821	1971-11-25
331	שמחה	גלעד	080118102	tmrmyt@example.org	9889489	1951-01-10
332	אשר	בכר	032510284	wyvsp@example.net	3341802	1999-11-19
333	דוד	חוסין	048201848	khyymvbrz@example.org	7270331	1951-06-19
334	הדר	לוי	041959747	yylh76@example.net	6288702	2000-09-23
335	מאיה	ברק	025895967	tkhg-ykhy@example.com	9425825	1987-05-10
336	הינדא	בוסקילה	084074476	ubd-l-qdr@example.com	1182586	1949-11-11
337	ליה	לוי	042219350	xlsyyd@example.net	4475809	1954-05-11
338	הלל	כהן	0568578169	tsbg@example.com	4774069	1949-05-11
339	רבקה	שפירא	0559485306	lynmyt@example.com	9418348	1953-02-16
340	אפרת	רובינשטיין	0565416983	tlvyn@example.net	9061347	1981-05-03
341	אדל	רוזנברג	097681702	ydv78@example.net	1625309	1984-11-02
342	יהונתן	סלימאן	0508672764	slyshrl@example.org	9976548	1950-10-08
343	משה	סואעד	047730867	rybytbvl@example.com	3523306	1958-04-14
344	תהל	עמאש	029152531	rbl15@example.com	6787579	2004-10-25
345	עדן	אלמוג	033823804	nmylr@example.com	9041081	1984-09-27
346	שירה	אוחיון	092271785	khnmrym@example.net	6422759	1999-04-26
347	הדר	כהן	044656974	zvbymyty@example.com	7796861	1963-08-31
348	רחל	משה	027383756	udvy@example.net	1666155	2005-08-19
349	יונתן	יוסף	092682791	dl19@example.com	1777397	1985-04-28
350	הללי	וייס	024682586	nghkhn@example.net	3336835	1970-04-26
351	הראל	שוויקי	049882380	cmlkh@example.org	2630930	2006-08-01
352	כפיר	סופר	095681653	lvynvh@example.net	6594971	1987-01-22
353	חנה	כהן	020999965	mlkh98@example.org	9565421	1950-09-29
354	טליה	כהן	087733571	gyvsp@example.net	4193763	1951-06-13
355	נחמה	לוי	032697401	tmrhrvsh@example.net	2059555	1995-07-30
356	הדר	דהן	0511321792	zvqnyn@example.com	8864416	2004-10-21
357	יאמן	רחמים	026511195	uslmn@example.org	1595291	1969-07-05
358	איילה	אהרן	028809154	zvhrshvshnh@example.com	9661615	1991-12-16
359	אדל	מאיר	0516796639	jtvytv@example.org	3459520	1977-11-01
360	רונה	פנחס	028948588	drvrydv@example.org	2450112	1990-07-06
361	מיאל	אביב	0523506740	nkhmhlymlk@example.org	7179554	1965-11-25
362	תהילה	אזולאי	0503154966	rvmyvqnyn@example.com	3511858	1977-06-24
363	אגם	פישר	090859688	qrvznpld@example.com	5474990	1971-09-06
364	ענבר	נסים	031977245	lyb39@example.org	1120657	1952-10-13
365	הניה	בן דוד	085963864	hvrvbytsshy-ly@example.com	5868107	1997-05-31
366	נוה	פאר	081606899	nvyhvkhnh@example.net	8464851	1949-12-15
367	נועה	סויסה	049662699	lyhvdb@example.org	7507204	1972-12-25
368	הדסה	סלומון	094457487	shlmhlyhv@example.org	7395909	1971-07-08
369	יעל	הררי	088863587	qkhtyb@example.com	5951753	1953-02-20
370	איתמר	אלטורי	0510343289	ydv69@example.org	6725493	1984-11-10
371	איילת	פלדמן	092132628	ptmh09@example.com	4966542	1952-04-05
372	שרה	יוסף	025489066	mzrkhyytmr@example.org	4233190	1968-01-09
373	נועה	אדלר	0527492836	mlkhln@example.net	3304666	1955-12-08
374	אמיתי	מלכה	098144299	mnkhmlh@example.org	4596279	1994-11-29
375	מלכה	פורמן	0534369513	shm-tvbvvh@example.net	4668462	1985-08-03
376	רחל	שפירא	0568247187	fmrm@example.net	7655732	2003-11-07
377	שוהם	פנחס	081933237	shmvnytskhq@example.org	5080279	1954-01-12
378	יעל	דהן	0538177394	mzrkhyyylh@example.net	9672661	1959-01-01
379	ישי	אסרף	0516433162	ynykhn@example.com	6159510	1969-04-17
380	יוסף	יעקב	0532465328	yvbl30@example.com	6161776	1986-04-14
381	חלא	אמסלם	047911704	gm54@example.org	5007115	1971-05-19
382	אביגיל	טל	080474254	yylh38@example.net	5702074	1977-12-27
383	יעקב	מנדל	096840024	qvpmnlyvr@example.net	7424394	1965-10-08
384	יחיא	אברמוביץ	084936341	shtyyngyh@example.com	9223836	1978-12-18
385	רות	אדרי	089832756	hqpln@example.org	5364623	1961-12-03
386	זינב	רוט	035261820	nlvy@example.org	5392761	1993-09-04
387	איתן	לוי	0511768797	tshtyyn@example.org	4661967	1999-05-09
388	שירה	עלי	047606615	prtskpyr@example.org	4512510	1975-01-17
389	מאיה	שרביט	023087041	olvy@example.com	3166119	1955-07-23
390	יעל	הופמן	0511616166	ugb@example.com	6243130	1966-05-17
391	אדל	בכר	087934250	khnbnymyn@example.com	2392695	1993-02-07
392	תמר	חסון	029038306	mvkhmd71@example.org	1394896	1982-02-19
393	אחינועם	טויטו	082056052	zybgy@example.com	6508968	1955-07-19
394	ליאל	בכר	0564201432	bytvnyhly@example.net	9710555	1992-09-12
395	לירן	אלמלח	025107195	yvntn96@example.org	4281479	1959-12-09
396	שירה	בר	030009958	bdrnhdbyr@example.org	6503994	1988-12-28
397	נגה	זינגר	025189957	flvy@example.com	7569511	1998-04-01
398	הדר	אזברגה	039508395	yshrlsvpr@example.org	2279581	1952-08-25
399	פאטמה	עמר	041615781	lyrzkhzn@example.org	8057505	1986-06-24
400	איליי	כהן	0569693854	pryydtsdvq@example.org	1567605	1952-10-25
401	אחמד	מלכה	0510206605	my14@example.com	8150026	2001-05-30
402	נריה	גל	020765043	rzmyty@example.net	1100492	1964-10-19
403	אורי	ח'טיב	0537206822	gvtmnbygyl@example.net	1593419	2005-11-01
1	דויד	לוי	0501234567	david@example.com	123456789	1990-05-01
2	מאיה	כהן	0509876543	maya@example.com	987654321	1985-12-11
3	נועה	בר	0504567890	noa@example.com	555444333	1993-07-21
\.


--
-- Data for Name: maintenance; Type: TABLE DATA; Schema: public; Owner: shira
--

COPY public.maintenance (maintenanceid, maintenancedate, description, mcost, carid) FROM stdin;
1	2025-02-10	Oil change and filter replacement	200.00	1
2	2025-02-20	Tire replacement	600.00	2
3	2025-03-01	Brake pad replacement	450.00	3
4	2025-01-25	Oil change	1073.73	175
5	2024-06-17	Tire replacement	911.76	108
6	2024-10-15	Oil change	781.03	215
7	2024-07-02	Battery replacement	552.22	55
8	2024-07-06	Tire replacement	165.25	256
9	2024-09-14	Transmission check	964.33	398
10	2025-03-05	Oil change	418.86	337
11	2024-06-25	Transmission check	826.61	384
12	2024-06-17	Brake inspection	418.42	22
13	2024-11-29	Brake inspection	744.22	363
14	2024-09-15	Brake inspection	555.02	49
15	2024-08-08	Tire replacement	257.84	208
16	2024-04-09	Battery replacement	522.69	170
17	2024-11-02	Oil change	516.92	200
18	2024-10-17	Battery replacement	843.98	84
19	2024-12-03	Transmission check	510.04	268
20	2024-04-21	Transmission check	1002.77	315
21	2024-06-15	Battery replacement	208.76	344
22	2024-11-18	Engine tune-up	752.74	122
23	2025-02-06	Transmission check	1067.76	229
24	2024-06-28	Transmission check	800.86	144
25	2024-05-13	Engine tune-up	317.20	368
26	2025-01-31	Oil change	567.31	44
27	2024-09-12	Transmission check	306.26	291
28	2024-11-08	Battery replacement	325.56	143
29	2024-07-12	Brake inspection	767.10	288
30	2024-07-04	Transmission check	328.16	284
31	2024-11-05	Brake inspection	1105.87	235
32	2024-07-16	Engine tune-up	385.92	249
33	2025-03-13	Engine tune-up	495.29	206
34	2025-01-04	Battery replacement	279.59	212
35	2025-01-02	Oil change	470.53	49
36	2025-01-22	Tire replacement	974.36	135
37	2025-02-27	Battery replacement	814.70	287
38	2024-07-20	Transmission check	1146.42	106
39	2025-01-25	Brake inspection	282.19	300
40	2024-07-08	Brake inspection	777.81	59
41	2024-09-13	Engine tune-up	470.11	26
42	2024-10-11	Engine tune-up	658.52	224
43	2024-07-29	Battery replacement	342.65	314
44	2024-04-12	Engine tune-up	868.31	229
45	2024-05-06	Brake inspection	1140.16	139
46	2025-03-25	Oil change	399.09	128
47	2024-10-19	Transmission check	548.35	200
48	2024-12-07	Battery replacement	821.74	278
49	2025-03-16	Oil change	653.81	27
50	2024-06-17	Brake inspection	341.22	286
51	2025-03-21	Tire replacement	610.49	369
52	2024-11-27	Tire replacement	985.67	4
53	2024-05-31	Engine tune-up	388.32	5
54	2024-04-14	Tire replacement	1018.78	359
55	2024-09-14	Brake inspection	1006.31	136
56	2025-01-10	Transmission check	751.99	337
57	2024-04-08	Engine tune-up	890.55	174
58	2024-04-09	Oil change	537.48	321
59	2025-03-02	Tire replacement	1062.11	75
60	2024-10-12	Transmission check	216.76	184
61	2024-09-09	Engine tune-up	1036.11	355
62	2024-06-01	Battery replacement	1100.58	42
63	2024-05-22	Engine tune-up	323.23	90
64	2024-08-04	Battery replacement	440.18	16
65	2025-03-14	Oil change	1085.22	264
66	2024-06-04	Battery replacement	540.08	203
67	2024-07-02	Tire replacement	782.67	185
68	2024-10-29	Brake inspection	235.30	134
69	2024-08-22	Transmission check	408.01	320
70	2024-04-29	Brake inspection	325.28	28
71	2024-05-21	Battery replacement	458.37	368
72	2024-04-10	Engine tune-up	214.54	263
73	2024-08-16	Tire replacement	570.63	44
74	2025-03-24	Tire replacement	672.08	130
75	2025-01-23	Battery replacement	237.85	118
76	2025-03-20	Brake inspection	518.53	146
77	2024-03-31	Battery replacement	284.01	5
78	2025-03-24	Engine tune-up	1091.69	235
79	2025-01-06	Tire replacement	742.76	117
80	2024-11-04	Oil change	176.33	244
81	2024-05-29	Brake inspection	766.53	159
82	2025-02-06	Brake inspection	469.53	66
83	2025-02-13	Battery replacement	1051.95	173
84	2024-08-20	Engine tune-up	472.75	387
85	2024-05-14	Brake inspection	512.62	143
86	2024-07-14	Transmission check	984.40	138
87	2024-05-13	Brake inspection	590.19	237
88	2024-11-30	Engine tune-up	616.78	311
89	2024-11-06	Oil change	871.30	179
90	2024-12-22	Brake inspection	911.70	244
91	2024-04-22	Brake inspection	181.34	164
92	2024-12-18	Tire replacement	878.27	301
93	2024-12-03	Battery replacement	1027.86	199
94	2024-08-28	Engine tune-up	937.46	237
95	2025-03-24	Transmission check	456.68	50
96	2024-04-17	Oil change	581.69	391
97	2024-06-17	Tire replacement	174.32	220
98	2024-09-16	Brake inspection	435.24	368
99	2024-09-08	Transmission check	207.44	135
100	2024-12-13	Brake inspection	375.98	39
101	2025-03-01	Battery replacement	595.98	384
102	2024-07-31	Engine tune-up	1111.28	330
103	2024-08-01	Engine tune-up	376.13	215
104	2024-11-09	Engine tune-up	583.11	140
105	2024-10-10	Tire replacement	217.05	119
106	2024-08-22	Tire replacement	995.47	217
107	2024-07-02	Tire replacement	1175.59	8
108	2024-11-04	Brake inspection	384.49	173
109	2024-09-01	Engine tune-up	620.88	91
110	2024-05-23	Brake inspection	1109.44	251
111	2025-01-28	Engine tune-up	425.20	196
112	2024-07-09	Tire replacement	724.30	290
113	2024-04-17	Tire replacement	173.64	383
114	2024-05-06	Transmission check	833.69	373
115	2024-05-13	Oil change	1143.20	232
116	2024-05-28	Brake inspection	871.47	198
117	2024-12-15	Tire replacement	295.54	352
118	2024-12-11	Oil change	486.28	366
119	2024-08-19	Tire replacement	1004.94	160
120	2025-03-10	Brake inspection	549.90	169
121	2024-09-24	Transmission check	394.91	51
122	2024-12-13	Transmission check	894.28	64
123	2024-05-28	Battery replacement	326.43	312
124	2024-09-26	Battery replacement	643.20	401
125	2024-05-16	Oil change	981.65	79
126	2024-06-21	Battery replacement	695.59	122
127	2024-11-21	Engine tune-up	806.72	148
128	2024-05-18	Tire replacement	1191.53	160
129	2024-09-17	Brake inspection	783.59	324
130	2025-02-27	Brake inspection	1017.42	160
131	2025-03-20	Tire replacement	681.99	159
132	2025-01-17	Tire replacement	854.32	215
133	2025-03-11	Oil change	1013.89	348
134	2024-06-14	Engine tune-up	1138.11	285
135	2024-04-03	Battery replacement	813.81	354
136	2025-03-21	Oil change	680.97	42
137	2024-06-06	Brake inspection	922.27	280
138	2024-06-12	Engine tune-up	1118.24	6
139	2025-03-17	Tire replacement	516.50	386
140	2025-02-02	Tire replacement	158.24	329
141	2024-06-13	Battery replacement	539.63	16
142	2024-05-05	Engine tune-up	1149.10	136
143	2024-07-08	Battery replacement	567.69	283
144	2025-02-02	Battery replacement	790.68	359
145	2024-04-26	Tire replacement	959.25	378
146	2024-05-16	Battery replacement	925.76	198
147	2025-02-07	Brake inspection	581.96	5
148	2024-04-28	Engine tune-up	923.32	196
149	2025-03-15	Brake inspection	645.30	250
150	2024-10-19	Tire replacement	792.61	380
151	2024-12-05	Transmission check	883.81	125
152	2024-06-22	Oil change	974.34	274
153	2024-04-30	Battery replacement	1146.75	310
154	2025-02-07	Brake inspection	317.79	135
155	2024-06-13	Battery replacement	1072.78	322
156	2024-04-30	Brake inspection	1088.25	162
157	2024-09-16	Oil change	725.27	262
158	2025-02-10	Oil change	820.76	231
159	2025-03-22	Transmission check	983.07	169
160	2024-10-08	Battery replacement	225.08	254
161	2025-01-02	Brake inspection	941.57	203
162	2024-07-21	Engine tune-up	288.56	393
163	2024-06-04	Tire replacement	207.08	293
164	2024-10-31	Transmission check	572.01	296
165	2025-03-19	Oil change	1075.57	212
166	2024-09-23	Engine tune-up	270.75	278
167	2025-02-16	Tire replacement	547.02	358
168	2024-07-01	Transmission check	969.33	253
169	2024-08-04	Tire replacement	171.85	302
170	2025-01-23	Transmission check	383.82	176
171	2024-06-21	Engine tune-up	995.22	177
172	2025-01-18	Battery replacement	810.59	272
173	2024-06-19	Brake inspection	652.70	272
174	2024-09-01	Battery replacement	575.20	308
175	2024-08-24	Battery replacement	423.52	46
176	2024-05-17	Battery replacement	736.40	326
177	2024-07-27	Brake inspection	561.96	248
178	2024-10-11	Tire replacement	302.39	228
179	2025-02-21	Tire replacement	665.70	308
180	2024-06-26	Transmission check	294.65	114
181	2024-09-19	Battery replacement	414.13	393
182	2024-10-15	Engine tune-up	584.48	107
183	2024-11-13	Battery replacement	890.23	341
184	2025-01-07	Battery replacement	164.13	400
185	2024-06-13	Brake inspection	797.36	368
186	2025-03-18	Oil change	445.01	22
187	2024-11-14	Oil change	740.98	157
188	2024-08-08	Brake inspection	1195.36	374
189	2025-02-07	Tire replacement	453.48	250
190	2024-07-31	Transmission check	1050.56	336
191	2024-04-14	Oil change	438.32	289
192	2025-02-11	Battery replacement	276.81	30
193	2024-08-10	Transmission check	1095.44	391
194	2024-10-22	Battery replacement	1115.80	282
195	2025-02-16	Oil change	1148.43	323
196	2024-08-19	Oil change	352.01	318
197	2024-12-28	Engine tune-up	946.05	201
198	2024-04-11	Engine tune-up	333.38	259
199	2024-03-29	Oil change	225.32	83
200	2024-10-15	Transmission check	734.76	91
201	2025-03-17	Brake inspection	359.69	140
202	2024-08-30	Battery replacement	354.44	302
203	2024-12-25	Battery replacement	871.10	222
204	2024-05-31	Engine tune-up	276.16	345
205	2025-03-10	Tire replacement	929.68	284
206	2024-07-24	Tire replacement	179.05	208
207	2024-06-01	Battery replacement	721.67	101
208	2024-09-18	Engine tune-up	332.11	8
209	2024-05-12	Tire replacement	326.13	51
210	2025-01-28	Oil change	1029.70	221
211	2024-04-09	Brake inspection	1049.00	98
212	2024-10-31	Engine tune-up	250.15	37
213	2024-05-08	Tire replacement	1003.00	221
214	2024-04-02	Brake inspection	844.56	306
215	2024-11-26	Transmission check	613.81	163
216	2025-02-10	Transmission check	1152.78	148
217	2024-04-16	Transmission check	995.13	5
218	2024-12-21	Engine tune-up	303.71	354
219	2024-06-14	Transmission check	1183.26	193
220	2024-07-15	Brake inspection	874.75	336
221	2024-10-13	Oil change	623.35	156
222	2024-10-12	Brake inspection	887.19	20
223	2024-10-06	Engine tune-up	1110.22	340
224	2024-07-12	Oil change	646.83	349
225	2024-10-26	Brake inspection	594.87	41
226	2024-06-13	Transmission check	1017.83	368
227	2025-03-13	Brake inspection	367.42	175
228	2024-09-20	Oil change	806.72	201
229	2024-07-10	Engine tune-up	184.35	93
230	2024-10-20	Engine tune-up	347.72	382
231	2024-12-26	Oil change	243.12	167
232	2024-08-05	Brake inspection	815.58	219
233	2025-03-23	Brake inspection	1149.11	270
234	2024-04-18	Oil change	753.39	345
235	2024-12-21	Tire replacement	462.18	320
236	2024-07-09	Brake inspection	796.01	28
237	2024-03-28	Battery replacement	503.72	226
238	2024-12-31	Transmission check	974.36	120
239	2025-03-15	Battery replacement	930.94	362
240	2024-11-28	Battery replacement	672.80	193
241	2024-10-07	Tire replacement	389.59	295
242	2024-10-26	Engine tune-up	1006.95	222
243	2024-05-26	Battery replacement	1016.96	21
244	2024-08-10	Battery replacement	359.40	242
245	2025-02-15	Brake inspection	732.07	89
246	2024-06-17	Oil change	229.64	343
247	2024-11-05	Tire replacement	226.56	203
248	2024-12-26	Transmission check	757.69	373
249	2024-11-04	Battery replacement	986.49	107
250	2024-05-30	Engine tune-up	712.82	96
251	2024-11-08	Brake inspection	471.53	220
252	2024-07-14	Transmission check	1036.99	76
253	2024-06-24	Oil change	868.96	186
254	2025-01-18	Engine tune-up	766.39	348
255	2024-11-22	Engine tune-up	495.61	37
256	2024-12-24	Oil change	1143.55	161
257	2025-03-15	Oil change	1003.24	13
258	2024-10-17	Transmission check	408.17	49
259	2025-01-26	Tire replacement	255.98	316
260	2024-11-13	Tire replacement	671.37	203
261	2024-08-17	Brake inspection	896.76	282
262	2024-05-17	Battery replacement	437.82	23
263	2024-06-22	Battery replacement	686.06	226
264	2024-06-22	Tire replacement	708.25	331
265	2024-06-07	Battery replacement	667.62	395
266	2024-06-11	Oil change	1091.60	117
267	2024-11-21	Engine tune-up	272.26	397
268	2024-11-03	Tire replacement	1143.44	291
269	2024-10-10	Tire replacement	1172.37	335
270	2024-10-26	Engine tune-up	640.91	49
271	2024-08-21	Tire replacement	304.54	301
272	2024-08-30	Engine tune-up	718.77	295
273	2024-10-18	Battery replacement	1116.86	298
274	2024-12-16	Tire replacement	213.75	177
275	2025-01-11	Brake inspection	767.33	385
276	2024-11-13	Transmission check	338.20	192
277	2024-07-23	Battery replacement	155.33	108
278	2024-09-25	Brake inspection	664.34	379
279	2024-05-14	Battery replacement	726.03	160
280	2025-03-01	Transmission check	1150.77	199
281	2025-02-10	Transmission check	266.42	140
282	2024-05-08	Engine tune-up	581.94	181
283	2024-08-15	Brake inspection	231.88	395
284	2024-07-28	Battery replacement	637.11	195
285	2025-01-26	Battery replacement	561.48	232
286	2024-07-21	Battery replacement	455.94	222
287	2024-10-16	Battery replacement	330.90	31
288	2024-05-08	Brake inspection	189.76	87
289	2025-01-24	Transmission check	985.10	369
290	2024-10-28	Tire replacement	984.31	326
291	2024-08-07	Tire replacement	779.66	393
292	2024-06-07	Transmission check	960.35	174
293	2025-02-18	Tire replacement	1070.78	185
294	2024-09-04	Brake inspection	237.91	385
295	2024-12-02	Brake inspection	805.08	16
296	2024-06-12	Oil change	1086.64	224
297	2024-08-17	Transmission check	317.63	11
298	2024-06-19	Brake inspection	271.77	169
299	2024-07-13	Battery replacement	480.89	339
300	2024-12-03	Battery replacement	875.09	248
301	2024-10-16	Oil change	629.34	44
302	2025-01-11	Tire replacement	713.96	142
303	2024-10-30	Engine tune-up	864.46	164
304	2024-06-30	Tire replacement	218.73	129
305	2025-01-22	Transmission check	1150.21	301
306	2024-09-07	Battery replacement	672.38	138
307	2024-08-07	Oil change	512.53	115
308	2024-10-29	Tire replacement	640.57	276
309	2024-08-14	Tire replacement	270.96	312
310	2024-04-25	Brake inspection	674.86	152
311	2024-09-13	Oil change	622.78	278
312	2024-06-28	Oil change	186.07	318
313	2025-01-28	Brake inspection	1077.55	331
314	2024-10-23	Engine tune-up	342.28	191
315	2025-02-07	Engine tune-up	986.15	15
316	2024-04-14	Tire replacement	358.46	207
317	2024-10-06	Battery replacement	183.35	370
318	2024-10-24	Oil change	581.26	12
319	2024-05-23	Battery replacement	972.90	124
320	2024-12-24	Battery replacement	600.11	116
321	2024-09-11	Oil change	1124.95	361
322	2024-08-10	Battery replacement	733.84	249
323	2025-03-20	Engine tune-up	957.67	156
324	2024-07-31	Battery replacement	189.01	301
325	2024-09-11	Engine tune-up	558.75	334
326	2024-07-30	Tire replacement	1187.81	243
327	2024-08-03	Battery replacement	979.49	334
328	2024-05-22	Oil change	723.00	59
329	2025-03-23	Transmission check	282.97	319
330	2025-01-01	Transmission check	783.50	9
331	2024-11-18	Transmission check	632.57	4
332	2024-05-04	Brake inspection	482.06	19
333	2024-05-05	Battery replacement	754.47	343
334	2025-01-07	Tire replacement	213.03	79
335	2024-05-12	Oil change	869.10	351
336	2024-07-09	Oil change	631.23	207
337	2024-09-07	Transmission check	945.70	15
338	2024-04-12	Oil change	516.64	185
339	2024-09-19	Brake inspection	838.69	391
340	2024-04-01	Brake inspection	995.49	161
341	2024-04-26	Brake inspection	641.72	227
342	2024-09-14	Brake inspection	749.48	285
343	2024-06-28	Transmission check	764.59	241
344	2024-09-08	Oil change	468.36	100
345	2024-05-13	Brake inspection	150.92	104
346	2024-06-13	Battery replacement	462.91	31
347	2024-05-15	Brake inspection	1171.44	303
348	2024-10-26	Transmission check	1058.27	269
349	2024-08-13	Engine tune-up	604.20	205
350	2024-10-25	Oil change	740.89	339
351	2024-07-23	Tire replacement	938.02	164
352	2024-12-21	Battery replacement	900.21	93
353	2024-04-23	Oil change	536.56	342
354	2025-03-20	Tire replacement	1032.01	171
355	2025-02-25	Transmission check	1004.53	178
356	2024-05-15	Transmission check	884.88	138
357	2024-08-06	Oil change	379.55	27
358	2024-04-17	Tire replacement	997.93	149
359	2024-06-15	Tire replacement	434.22	105
360	2024-06-05	Engine tune-up	733.48	364
361	2024-09-25	Engine tune-up	1061.73	76
362	2025-01-27	Brake inspection	886.95	296
363	2024-08-22	Transmission check	652.82	175
364	2025-01-25	Transmission check	1156.49	20
365	2024-04-20	Battery replacement	252.53	338
366	2024-04-12	Tire replacement	309.57	124
367	2024-11-19	Battery replacement	986.29	270
368	2024-11-06	Oil change	341.54	277
369	2024-04-23	Transmission check	500.18	251
370	2024-08-10	Battery replacement	444.67	289
371	2024-07-24	Brake inspection	627.01	290
372	2024-10-22	Transmission check	465.49	207
373	2024-08-05	Brake inspection	1095.92	68
374	2024-09-25	Battery replacement	750.04	49
375	2025-02-03	Transmission check	964.20	282
376	2025-02-17	Brake inspection	673.98	101
377	2025-01-13	Oil change	483.25	276
378	2024-08-11	Engine tune-up	820.57	304
379	2025-02-07	Tire replacement	981.00	119
380	2025-03-12	Engine tune-up	1025.25	161
381	2025-01-07	Brake inspection	232.02	354
382	2024-03-28	Tire replacement	587.86	59
383	2025-01-27	Engine tune-up	967.01	277
384	2024-12-11	Brake inspection	917.11	306
385	2025-01-25	Battery replacement	1178.37	305
386	2024-10-15	Brake inspection	429.55	308
387	2024-05-04	Tire replacement	181.10	336
388	2024-04-10	Oil change	1163.07	66
389	2024-07-14	Battery replacement	1153.33	328
390	2024-09-17	Oil change	673.91	117
391	2024-10-19	Tire replacement	724.61	379
392	2024-12-15	Oil change	1199.25	337
393	2025-01-04	Brake inspection	817.19	179
394	2024-07-03	Engine tune-up	971.33	19
395	2024-10-11	Transmission check	1150.40	131
396	2024-09-10	Brake inspection	730.81	133
397	2024-11-27	Engine tune-up	477.40	374
398	2024-10-29	Brake inspection	953.02	238
399	2024-05-02	Oil change	195.37	43
400	2024-10-30	Transmission check	628.93	163
401	2025-02-28	Brake inspection	626.08	153
402	2024-05-05	Battery replacement	228.44	365
403	2024-09-29	Transmission check	704.61	321
\.


--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: shira
--

COPY public.payment (paymentid, paymentdate, amount, paymentmethod) FROM stdin;
1	2025-03-01	320.50	Credit
2	2025-03-02	150.00	Cash
3	2025-03-03	270.75	PayPal
4	2025-11-07	206.72	Bank Transfer
5	2025-09-23	278.55	Credit
6	2025-05-01	937.29	Bit
7	2025-06-29	352.28	Credit
8	2025-04-04	217.22	Bank Transfer
9	2025-09-12	263.12	Credit
10	2025-09-10	762.82	Cash
11	2025-10-20	101.88	Cash
12	2025-12-07	979.45	Credit
13	2025-04-23	490.15	PayPal
14	2025-08-13	694.60	Bit
15	2025-09-30	127.50	Cash
16	2025-10-12	231.75	Bit
17	2025-09-23	148.74	Cash
18	2025-06-11	669.33	Credit
19	2025-10-23	621.47	Bank Transfer
20	2025-12-06	161.79	Cash
21	2025-09-27	378.06	Bit
22	2025-11-30	425.64	Bank Transfer
23	2025-07-02	618.33	Bank Transfer
24	2026-02-25	198.00	Bank Transfe
25	2025-02-22	145.00	PayPal
26	2024-11-10	961.00	Bank Transfe
27	2024-12-31	485.00	Bit
28	2024-08-13	372.00	Cash
29	2024-10-08	822.00	Bank Transfe
30	2024-08-25	598.00	Bit
31	2025-09-12	225.00	Cash
32	2025-01-28	208.00	Bit
33	2024-02-06	102.00	Bank Transfe
34	2025-02-11	118.00	PayPal
35	2025-08-29	238.00	PayPal
36	2025-04-15	796.00	Cash
37	2026-01-18	811.00	PayPal
38	2025-02-01	709.00	Credit
39	2025-05-21	867.00	PayPal
40	2024-06-09	655.00	Bit
41	2024-07-09	168.00	Bit
42	2025-08-23	627.00	Cash
43	2025-04-01	111.00	Cash
44	2025-11-09	151.00	Credit
45	2025-02-13	402.00	Bank Transfe
46	2024-10-31	592.00	Credit
47	2024-05-30	643.00	Cash
48	2024-03-29	307.00	Bank Transfe
49	2025-07-06	568.00	Bit
50	2025-09-10	479.00	PayPal
51	2025-03-29	632.00	Credit
52	2024-10-26	875.00	Cash
53	2025-01-15	392.00	Credit
54	2025-06-29	408.00	Cash
55	2024-01-10	418.00	Credit
56	2024-11-17	215.00	Credit
57	2024-11-21	799.00	Cash
58	2024-07-08	364.00	Cash
59	2025-11-07	635.00	PayPal
60	2025-06-29	443.00	Credit
61	2026-04-03	239.00	Bank Transfe
62	2024-06-28	918.00	Credit
63	2025-01-10	971.00	Bit
64	2026-08-01	886.00	PayPal
65	2024-03-09	181.00	Cash
66	2024-12-29	484.00	Bank Transfe
67	2025-08-18	931.00	Cash
68	2024-06-28	475.00	Bank Transfe
69	2024-06-17	279.00	Bit
70	2025-05-28	132.00	Bit
71	2025-02-12	479.00	Bit
72	2026-02-28	841.00	Credit
73	2024-04-08	571.00	Credit
74	2024-10-09	886.00	Cash
75	2024-11-19	385.00	PayPal
76	2025-07-12	773.00	Cash
77	2025-05-04	389.00	Bit
78	2024-10-13	761.00	PayPal
79	2025-09-02	252.00	PayPal
80	2026-03-17	138.00	Bit
81	2026-11-03	936.00	Bit
82	2025-01-31	597.00	Bit
83	2025-05-23	880.00	Bit
84	2025-09-03	982.00	Bank Transfe
85	2024-08-26	276.00	Bank Transfe
86	2024-11-13	551.00	Cash
87	2025-10-24	546.00	Bank Transfe
88	2025-01-06	857.00	Credit
89	2025-10-23	419.00	Credit
90	2024-01-12	350.00	Bank Transfe
91	2025-09-09	252.00	Bit
92	2025-11-29	782.00	PayPal
93	2024-11-14	927.00	Cash
94	2025-10-03	868.00	PayPal
95	2024-11-13	876.00	Cash
96	2025-04-12	205.00	Credit
97	2025-06-04	671.00	Bit
98	2025-04-24	755.00	PayPal
99	2026-01-23	780.00	Cash
100	2025-04-26	405.00	Bank Transfe
101	2024-02-08	790.00	Cash
102	2026-01-19	287.00	PayPal
103	2025-06-12	775.00	Credit
104	2025-02-27	632.00	Cash
105	2025-11-20	590.00	Bank Transfe
106	2025-12-28	752.00	Bit
107	2024-08-13	105.00	Credit
108	2026-02-18	973.00	Cash
109	2024-05-30	196.00	Bank Transfe
110	2024-10-11	276.00	Bank Transfe
111	2025-06-10	657.00	Cash
112	2025-08-21	831.00	Bank Transfe
113	2025-06-05	883.00	PayPal
114	2025-03-10	505.00	Credit
115	2025-04-30	286.00	PayPal
116	2025-09-19	696.00	Bit
117	2025-07-19	461.00	Cash
118	2024-10-29	945.00	Bank Transfe
119	2025-11-04	458.00	Bit
120	2025-02-08	983.00	Bit
121	2024-09-25	415.00	Bit
122	2026-02-21	567.00	PayPal
123	2025-09-11	116.00	Bit
124	2025-03-08	871.00	Credit
125	2024-08-26	642.00	Bank Transfe
126	2025-11-03	932.00	Cash
127	2025-09-15	368.00	Bank Transfe
128	2026-01-13	994.00	Credit
129	2024-11-19	280.00	Bank Transfe
130	2024-09-29	680.00	Cash
131	2025-03-07	573.00	PayPal
132	2025-08-04	794.00	Bit
133	2025-09-28	800.00	Bit
134	2026-05-01	923.00	Bank Transfe
135	2024-09-29	586.00	Credit
136	2024-04-28	302.00	Credit
137	2026-02-25	775.00	Bank Transfe
138	2024-12-05	345.00	PayPal
139	2025-06-13	337.00	Cash
140	2024-06-05	106.00	Bit
141	2024-05-09	755.00	PayPal
142	2024-10-08	944.00	Credit
143	2025-09-30	856.00	Cash
144	2024-10-13	832.00	Credit
145	2024-02-05	412.00	Credit
146	2024-07-08	396.00	Bit
147	2025-12-27	891.00	PayPal
148	2025-07-27	111.00	Bank Transfe
149	2024-05-16	651.00	Bit
150	2025-11-28	239.00	Credit
151	2024-06-05	114.00	Bank Transfe
152	2025-06-12	183.00	Bank Transfe
153	2024-04-15	697.00	Credit
154	2024-10-17	748.00	PayPal
155	2024-06-10	717.00	Credit
156	2025-01-26	949.00	Credit
157	2026-02-17	453.00	Credit
158	2026-01-21	985.00	PayPal
159	2025-09-10	281.00	Cash
160	2024-08-22	946.00	Cash
161	2025-02-07	461.00	Bit
162	2024-08-17	367.00	Bank Transfe
163	2026-05-01	376.00	Bank Transfe
164	2024-12-11	345.00	Cash
165	2025-04-30	563.00	Cash
166	2025-05-08	851.00	Bit
167	2024-04-09	228.00	Cash
168	2025-11-03	895.00	Bank Transfe
169	2025-09-24	345.00	Credit
170	2025-03-16	640.00	PayPal
171	2025-10-18	451.00	Bank Transfe
172	2026-10-03	179.00	Cash
173	2025-11-17	769.00	Cash
174	2025-03-15	374.00	Bank Transfe
175	2024-10-22	986.00	PayPal
176	2026-01-16	343.00	Credit
177	2025-02-28	721.00	Bit
178	2025-07-14	815.00	Cash
179	2025-06-29	488.00	Bit
180	2025-01-09	960.00	Bank Transfe
181	2024-05-27	613.00	Bank Transfe
182	2024-11-24	558.00	Bit
183	2024-09-04	633.00	Bank Transfe
184	2024-10-27	445.00	PayPal
185	2024-12-05	810.00	Bank Transfe
186	2025-12-19	118.00	Bit
187	2025-06-26	893.00	PayPal
188	2024-03-28	708.00	PayPal
189	2025-02-05	747.00	PayPal
190	2026-03-26	757.00	Cash
191	2026-02-22	530.00	Bank Transfe
192	2024-06-08	706.00	Bit
193	2024-11-21	213.00	Bank Transfe
194	2025-11-05	161.00	Cash
195	2025-07-03	343.00	Bank Transfe
196	2025-03-27	938.00	Credit
197	2024-06-27	590.00	Credit
198	2025-11-02	309.00	Cash
199	2024-09-22	536.00	Bit
200	2025-01-08	830.00	Bit
201	2024-05-17	157.00	Cash
202	2025-10-06	661.00	Credit
203	2025-01-22	494.00	Bit
204	2024-10-27	548.00	PayPal
205	2025-06-21	949.00	Bank Transfe
206	2024-04-11	346.00	Cash
207	2024-03-08	220.00	Bit
208	2024-01-05	366.00	PayPal
209	2025-04-15	787.00	PayPal
210	2024-04-16	403.00	Bit
211	2024-12-14	443.00	PayPal
212	2024-11-17	794.00	Bit
213	2025-06-02	229.00	Bank Transfe
214	2026-03-02	552.00	Bank Transfe
215	2025-08-27	435.00	PayPal
216	2024-06-11	929.00	Bank Transfe
217	2025-10-14	320.00	Bank Transfe
218	2025-07-30	930.00	Cash
219	2025-02-25	141.00	Credit
220	2024-03-30	961.00	Credit
221	2024-02-11	123.00	Cash
222	2024-06-18	636.00	Bit
223	2024-06-29	687.00	PayPal
224	2026-01-28	437.00	Bank Transfe
225	2024-06-07	795.00	Credit
226	2026-02-26	162.00	Credit
227	2024-06-16	506.00	Cash
228	2024-11-16	578.00	Cash
229	2025-09-10	779.00	PayPal
230	2025-10-26	706.00	Bank Transfe
231	2024-11-25	541.00	Cash
232	2024-12-11	390.00	Credit
233	2025-03-03	238.00	PayPal
234	2024-10-10	726.00	Bit
235	2026-07-01	917.00	Bank Transfe
236	2026-02-28	158.00	Bank Transfe
237	2024-06-25	804.00	Bit
238	2024-12-26	638.00	Credit
239	2026-01-03	814.00	Credit
240	2024-12-22	844.00	Credit
241	2025-01-02	899.00	Bank Transfe
242	2024-03-08	846.00	Cash
243	2025-03-31	251.00	Cash
244	2024-12-31	890.00	Bit
245	2024-06-18	639.00	Bank Transfe
246	2025-08-27	685.00	Bit
247	2025-09-20	323.00	Credit
248	2025-11-03	668.00	Credit
249	2026-01-16	230.00	PayPal
250	2024-05-28	569.00	Credit
251	2025-10-27	858.00	Cash
252	2024-04-07	659.00	Bit
253	2025-09-01	125.00	Bank Transfe
254	2024-06-04	274.00	Bank Transfe
255	2026-09-03	482.00	PayPal
256	2025-01-16	469.00	Bank Transfe
257	2024-04-20	887.00	Bank Transfe
258	2024-05-10	355.00	Bank Transfe
259	2024-05-21	704.00	Cash
260	2025-12-18	387.00	Cash
261	2025-06-08	463.00	PayPal
262	2024-04-30	531.00	Bit
263	2025-07-21	587.00	Credit
264	2025-07-13	620.00	Credit
265	2024-04-27	621.00	Credit
266	2026-01-22	944.00	Bank Transfe
267	2025-10-12	950.00	PayPal
268	2024-08-11	123.00	Bank Transfe
269	2025-10-02	443.00	Credit
270	2024-06-04	445.00	Bit
271	2024-05-23	491.00	Credit
272	2025-05-11	144.00	Bit
273	2025-06-19	476.00	PayPal
274	2024-10-15	495.00	Bank Transfe
275	2025-01-07	289.00	PayPal
276	2025-01-15	640.00	Cash
277	2024-11-21	838.00	Bank Transfe
278	2025-10-30	383.00	Bank Transfe
279	2026-02-15	214.00	Bank Transfe
280	2025-07-21	634.00	Bank Transfe
281	2025-05-29	834.00	Credit
282	2025-03-17	513.00	Credit
283	2024-03-30	718.00	Bank Transfe
284	2024-06-15	564.00	Credit
285	2025-02-14	732.00	PayPal
286	2025-09-28	247.00	PayPal
287	2025-04-08	526.00	Credit
288	2026-01-20	669.00	PayPal
289	2025-07-27	567.00	Cash
290	2025-10-25	814.00	Bank Transfe
291	2024-07-20	646.00	PayPal
292	2024-10-19	431.00	PayPal
293	2025-01-21	385.00	Bit
294	2025-09-03	595.00	Cash
295	2025-12-29	482.00	Bit
296	2025-07-20	131.00	Cash
297	2024-12-16	464.00	PayPal
298	2025-09-11	910.00	Bank Transfe
299	2025-11-22	234.00	Credit
300	2024-09-13	493.00	Bank Transfe
301	2024-11-27	359.00	PayPal
302	2025-06-18	562.00	Credit
303	2025-05-04	335.00	Bank Transfe
304	2025-05-05	422.00	PayPal
305	2024-04-16	700.00	Credit
306	2025-01-18	307.00	Bit
307	2024-05-08	377.00	Credit
308	2025-02-03	505.00	Bit
309	2024-11-23	544.00	Bit
310	2026-03-18	702.00	Cash
311	2025-04-14	205.00	PayPal
312	2025-12-03	407.00	Credit
313	2024-04-20	365.00	Bank Transfe
314	2026-05-02	397.00	Credit
315	2025-02-17	503.00	Cash
316	2025-07-21	224.00	PayPal
317	2025-02-04	620.00	Bit
318	2024-10-18	981.00	PayPal
319	2024-08-04	797.00	Credit
320	2025-09-03	436.00	Bit
321	2025-10-21	413.00	PayPal
322	2025-07-09	322.00	PayPal
323	2025-01-23	326.00	Cash
324	2025-08-07	911.00	Cash
325	2025-01-30	932.00	Credit
326	2024-10-15	975.00	Bit
327	2024-09-15	729.00	Cash
328	2024-07-16	989.00	PayPal
329	2025-12-02	929.00	PayPal
330	2025-09-14	698.00	Cash
331	2024-07-30	390.00	Credit
332	2026-03-20	730.00	Cash
333	2025-06-01	100.00	Bit
334	2025-07-12	448.00	Credit
335	2025-09-29	712.00	Credit
336	2025-07-24	697.00	Cash
337	2024-05-31	202.00	Bit
338	2026-03-02	184.00	Bank Transfe
339	2025-11-20	399.00	Bank Transfe
340	2025-05-08	396.00	Credit
341	2025-02-15	198.00	PayPal
342	2025-04-13	425.00	Credit
343	2024-04-15	469.00	Bank Transfe
344	2024-11-10	382.00	Bank Transfe
345	2025-07-08	322.00	Cash
346	2025-02-13	291.00	Credit
347	2026-01-26	968.00	Bit
348	2024-03-06	246.00	Cash
349	2026-02-16	249.00	Cash
350	2024-11-29	831.00	Credit
351	2025-07-18	610.00	Bank Transfe
352	2024-04-05	695.00	Bit
353	2025-08-24	322.00	Bank Transfe
354	2025-09-16	382.00	PayPal
355	2025-11-20	842.00	Cash
356	2024-11-10	472.00	Bank Transfe
357	2025-11-09	616.00	Cash
358	2026-01-18	486.00	Cash
359	2024-10-21	662.00	Bank Transfe
360	2025-12-09	356.00	PayPal
361	2024-05-27	756.00	Credit
362	2025-01-15	357.00	Credit
363	2025-09-17	908.00	PayPal
364	2024-11-07	846.00	Cash
365	2024-05-29	853.00	Cash
366	2025-05-01	295.00	Credit
367	2024-02-11	600.00	Bit
368	2025-03-23	954.00	PayPal
369	2025-07-17	199.00	Bit
370	2026-02-20	137.00	Bank Transfe
371	2025-01-06	987.00	PayPal
372	2025-01-24	353.00	Credit
373	2025-05-25	990.00	Bank Transfe
374	2024-12-12	857.00	PayPal
375	2024-07-15	574.00	PayPal
376	2025-11-18	364.00	Credit
377	2024-12-04	907.00	Bank Transfe
378	2024-04-13	530.00	PayPal
379	2024-07-11	238.00	Bank Transfe
380	2025-12-06	309.00	Bank Transfe
381	2025-04-09	256.00	Bit
382	2025-06-10	676.00	Bit
383	2024-04-21	283.00	Cash
384	2026-02-19	793.00	Cash
385	2025-07-24	336.00	Credit
386	2025-08-07	900.00	Bit
387	2025-05-09	434.00	Bank Transfe
388	2025-03-08	926.00	Bank Transfe
389	2025-04-12	101.00	Cash
390	2025-06-12	848.00	Credit
391	2024-12-11	891.00	Cash
392	2025-12-09	170.00	Cash
393	2024-06-08	235.00	Bank Transfe
394	2025-09-08	111.00	Bank Transfe
395	2024-12-06	127.00	Cash
396	2026-03-15	747.00	PayPal
\.


--
-- Data for Name: rental; Type: TABLE DATA; Schema: public; Owner: shira
--

COPY public.rental (rentalid, startdate, enddate, totalcost, customerid, carid, paymentid) FROM stdin;
4	2024-04-22	2024-04-28	2297.64	23	166	21
5	2024-08-20	2024-08-21	366.36	254	5	14
6	2024-10-18	2024-10-25	1440.39	359	15	6
7	2025-01-18	2025-01-19	250.36	6	346	5
8	2025-03-15	2025-03-17	423.28	274	289	15
9	2024-11-12	2024-11-16	1724.60	77	167	6
10	2024-11-25	2024-12-05	4945.80	388	36	17
11	2024-09-09	2024-09-15	1614.42	369	149	18
12	2024-12-20	2024-12-21	317.08	66	45	23
13	2024-10-01	2024-10-03	693.20	201	100	1
14	2024-12-20	2024-12-23	1388.07	357	296	16
15	2024-09-13	2024-09-21	3570.08	11	381	23
16	2024-07-22	2024-07-31	1135.62	329	229	13
17	2024-04-17	2024-04-22	772.30	3	341	13
18	2024-06-16	2024-06-22	2909.76	151	116	15
19	2024-11-14	2024-11-16	561.76	336	13	4
20	2024-05-07	2024-05-13	2037.90	83	187	5
21	2025-03-06	2025-03-10	1345.32	240	396	20
22	2024-11-15	2024-11-18	1046.13	237	394	17
23	2024-05-04	2024-05-12	3847.84	112	285	12
24	2024-11-26	2024-12-03	2625.21	215	361	4
25	2025-01-31	2025-02-03	447.66	381	284	11
26	2024-05-10	2024-05-20	4545.60	163	109	16
27	2024-05-13	2024-05-15	749.08	96	308	7
28	2024-07-27	2024-08-01	1960.55	90	97	6
29	2025-02-25	2025-03-06	4085.10	362	363	19
30	2024-09-30	2024-10-05	617.10	169	14	6
31	2024-05-18	2024-05-27	2851.20	230	60	9
32	2025-01-26	2025-01-31	2197.80	122	17	2
33	2024-07-11	2024-07-14	1006.71	256	216	5
34	2024-08-06	2024-08-08	726.08	376	269	12
35	2025-02-27	2025-03-09	2646.70	305	63	13
36	2024-05-30	2024-06-09	4289.60	111	207	9
37	2024-06-22	2024-06-29	1615.32	52	29	15
38	2024-06-27	2024-07-06	2231.64	289	57	16
39	2024-12-29	2025-01-04	1062.48	14	252	1
40	2024-07-11	2024-07-12	245.00	322	264	11
41	2024-11-30	2024-12-07	1501.99	383	261	19
42	2024-10-01	2024-10-02	397.17	391	104	20
43	2025-03-10	2025-03-15	2048.40	335	181	6
44	2025-02-21	2025-02-25	1662.88	341	271	10
45	2024-06-25	2024-06-26	380.92	5	245	16
46	2024-09-19	2024-09-23	1220.80	234	348	1
47	2025-02-24	2025-02-25	292.26	319	249	21
48	2024-12-31	2025-01-08	1580.48	355	160	23
49	2024-12-26	2024-12-28	277.46	311	358	17
50	2025-01-11	2025-01-12	172.87	12	71	20
51	2024-10-26	2024-10-28	372.12	60	350	4
52	2024-12-09	2024-12-15	692.82	27	115	16
53	2025-01-25	2025-02-02	1625.60	139	339	11
54	2024-09-14	2024-09-17	312.06	375	69	4
55	2024-11-13	2024-11-20	2598.82	233	83	17
56	2024-08-26	2024-08-29	821.37	218	246	3
57	2024-06-30	2024-07-09	2469.78	116	267	9
58	2024-03-31	2024-04-05	890.85	18	243	19
59	2024-11-29	2024-12-08	3623.85	20	225	5
60	2024-10-26	2024-10-29	1325.73	140	136	1
61	2024-12-17	2024-12-22	1922.25	368	274	3
62	2025-02-23	2025-02-28	2435.80	104	209	11
63	2024-09-02	2024-09-03	467.28	64	321	2
64	2024-05-21	2024-05-30	4048.65	141	230	9
65	2024-09-24	2024-09-29	1982.25	288	194	1
66	2024-04-19	2024-04-27	1906.56	89	134	15
67	2024-08-06	2024-08-11	918.65	303	52	19
68	2024-08-27	2024-08-31	1846.32	174	288	6
69	2025-03-17	2025-03-21	654.24	28	10	21
70	2024-04-28	2024-05-08	2478.20	86	306	20
71	2024-04-13	2024-04-17	798.12	278	106	17
72	2024-08-21	2024-08-24	573.96	74	22	7
73	2024-12-10	2024-12-15	649.65	354	352	7
74	2024-09-13	2024-09-20	2868.39	238	113	9
75	2024-08-20	2024-08-25	1271.00	188	304	18
76	2024-08-06	2024-08-09	302.13	120	326	16
77	2025-01-27	2025-01-28	359.32	161	218	19
78	2024-06-08	2024-06-13	1629.45	129	234	10
79	2025-01-18	2025-01-20	983.92	48	12	13
80	2024-06-08	2024-06-16	3512.56	361	41	11
81	2024-09-29	2024-10-04	2002.00	313	333	23
82	2024-12-18	2024-12-19	318.17	7	58	5
83	2024-07-18	2024-07-20	220.10	168	195	10
84	2024-07-08	2024-07-12	636.64	323	369	8
85	2024-08-24	2024-08-26	966.44	185	282	15
86	2025-03-16	2025-03-21	577.45	327	317	10
87	2024-07-23	2024-07-28	1788.70	166	24	6
88	2025-02-03	2025-02-13	4745.70	105	402	14
89	2025-01-20	2025-01-29	3805.38	183	280	16
90	2024-06-19	2024-06-24	1204.70	224	278	20
91	2024-11-09	2024-11-12	310.92	78	400	12
92	2024-11-03	2024-11-05	518.18	348	64	1
93	2025-01-17	2025-01-22	1973.10	50	217	5
94	2024-12-16	2024-12-24	1432.88	1	169	5
95	2024-07-27	2024-07-29	612.12	167	177	10
96	2025-02-01	2025-02-10	4092.03	128	171	14
97	2024-10-28	2024-10-29	162.92	173	20	1
98	2024-10-26	2024-10-28	443.42	150	107	22
99	2024-08-12	2024-08-19	2336.74	103	332	5
100	2024-05-06	2024-05-11	1163.05	75	387	6
101	2024-10-26	2024-10-28	586.48	56	197	7
102	2024-09-30	2024-10-03	1328.82	293	21	12
103	2024-06-12	2024-06-18	2943.18	309	270	5
104	2025-02-01	2025-02-09	2849.36	115	219	22
105	2025-01-27	2025-01-28	459.37	231	395	14
106	2024-08-28	2024-09-02	662.65	76	145	10
107	2024-06-01	2024-06-02	304.88	316	231	12
108	2024-04-28	2024-05-03	534.40	221	213	4
109	2024-10-03	2024-10-12	3873.06	386	239	9
110	2024-11-09	2024-11-13	665.76	340	190	1
111	2025-02-03	2025-02-05	644.10	146	299	12
112	2024-06-06	2024-06-07	251.95	306	386	16
113	2024-04-15	2024-04-20	1871.95	58	359	23
114	2024-05-25	2024-05-31	2338.38	149	183	13
115	2025-03-16	2025-03-20	600.00	126	2	13
116	2024-04-17	2024-04-24	1571.85	387	331	22
117	2024-12-30	2025-01-09	3315.40	317	38	21
118	2024-10-13	2024-10-19	1255.50	156	111	22
119	2024-05-23	2024-05-27	1799.04	378	330	4
120	2024-04-21	2024-05-01	3875.00	82	279	15
121	2024-04-06	2024-04-14	3405.76	246	311	3
122	2024-06-15	2024-06-24	3046.14	337	62	19
123	2024-08-31	2024-09-04	1885.28	344	357	2
124	2024-08-04	2024-08-08	1559.56	379	398	18
125	2024-10-29	2024-10-31	722.74	181	266	16
126	2024-03-31	2024-04-08	1891.76	206	276	4
127	2025-03-09	2025-03-11	703.26	162	32	3
128	2024-11-20	2024-11-26	1410.30	258	49	19
129	2024-07-17	2024-07-21	1769.56	302	119	5
130	2025-01-19	2025-01-25	1913.70	101	364	13
131	2025-02-01	2025-02-04	1123.83	326	47	21
132	2024-12-17	2024-12-24	2928.24	186	122	5
133	2024-12-05	2024-12-12	2359.35	204	33	3
134	2025-03-10	2025-03-17	2709.63	265	6	6
135	2024-07-14	2024-07-23	3377.16	197	255	23
136	2024-10-16	2024-10-20	765.08	191	148	17
137	2024-11-11	2024-11-14	498.06	73	376	5
138	2024-09-17	2024-09-23	2866.86	40	322	17
139	2024-11-26	2024-11-28	647.76	275	272	16
140	2024-07-14	2024-07-21	3384.36	232	335	7
141	2024-10-12	2024-10-20	1858.16	273	19	23
142	2024-07-15	2024-07-21	2984.88	330	211	20
143	2025-01-12	2025-01-22	1043.50	208	390	18
144	2024-06-30	2024-07-07	1550.85	134	39	4
145	2024-12-06	2024-12-15	1474.20	370	186	2
146	2024-03-29	2024-03-31	342.90	8	403	21
147	2024-12-06	2024-12-12	1031.10	321	206	15
148	2025-02-05	2025-02-11	947.28	127	18	5
149	2024-09-07	2024-09-14	1309.07	198	129	22
150	2024-12-17	2024-12-27	2229.00	257	303	12
151	2024-10-14	2024-10-19	668.60	15	315	5
152	2024-11-26	2024-11-28	257.04	300	222	20
153	2024-07-26	2024-07-29	693.06	135	373	8
154	2024-07-15	2024-07-20	2134.25	125	247	21
155	2024-09-16	2024-09-18	854.74	37	110	19
156	2025-02-07	2025-02-10	661.86	124	281	22
157	2025-03-01	2025-03-09	1861.76	44	328	23
158	2024-12-09	2024-12-16	2987.18	79	353	19
159	2025-02-28	2025-03-08	1572.56	200	338	1
160	2024-12-19	2024-12-27	3508.80	202	130	1
161	2024-05-04	2024-05-05	153.55	142	93	23
162	2024-12-22	2024-12-29	1449.07	372	56	21
163	2025-02-18	2025-02-25	1324.96	271	101	23
164	2025-01-09	2025-01-17	2086.00	205	372	5
165	2024-05-21	2024-05-22	239.37	239	99	20
166	2024-12-03	2024-12-09	744.84	33	212	18
167	2024-05-16	2024-05-20	1279.04	325	354	5
168	2025-03-09	2025-03-13	1350.16	346	88	14
169	2025-02-18	2025-02-25	2356.20	55	370	1
170	2024-04-30	2024-05-01	423.02	154	143	22
171	2024-06-07	2024-06-11	1319.88	236	388	23
172	2024-04-08	2024-04-15	722.19	298	295	20
173	2024-04-07	2024-04-16	3823.02	94	152	21
174	2025-01-23	2025-02-01	3878.46	314	54	15
175	2024-12-16	2024-12-17	360.32	137	223	20
176	2024-08-19	2024-08-28	2526.57	394	23	13
177	2024-12-19	2024-12-22	375.63	35	81	9
178	2024-12-12	2024-12-13	267.44	41	204	16
179	2024-06-06	2024-06-16	1670.60	102	92	9
180	2024-05-19	2024-05-21	998.86	382	360	7
181	2024-06-08	2024-06-10	576.38	398	242	1
182	2024-06-22	2024-06-23	455.80	331	268	19
183	2024-11-04	2024-11-06	687.14	4	128	13
184	2024-04-08	2024-04-12	1904.52	19	343	14
185	2025-01-17	2025-01-22	1014.10	85	96	21
186	2024-06-28	2024-07-07	4076.82	339	214	9
187	2024-10-17	2024-10-25	1250.16	155	78	13
188	2024-11-25	2024-12-01	1358.16	119	210	14
189	2024-04-06	2024-04-12	1198.62	157	154	18
190	2025-02-10	2025-02-19	2903.31	353	301	16
191	2024-07-24	2024-08-01	1841.36	30	309	17
192	2024-03-29	2024-03-31	415.24	61	75	14
193	2024-08-16	2024-08-17	227.45	36	300	22
194	2024-04-17	2024-04-22	856.70	402	103	21
195	2024-09-21	2024-09-30	1912.68	31	215	6
196	2024-12-07	2024-12-15	2399.36	80	342	23
197	2024-11-27	2024-12-07	4839.90	324	199	7
198	2024-10-26	2024-10-29	493.20	358	316	15
199	2024-04-01	2024-04-11	4240.80	108	102	5
200	2024-10-31	2024-11-05	1694.20	403	67	14
201	2025-03-13	2025-03-23	3327.20	216	256	14
202	2024-03-27	2024-04-06	2183.90	222	26	21
203	2024-05-11	2024-05-17	787.92	147	140	6
204	2025-01-02	2025-01-11	936.00	352	337	11
205	2024-10-20	2024-10-24	1072.68	299	323	2
206	2025-02-25	2025-03-06	4351.23	342	334	3
207	2024-07-17	2024-07-19	942.58	244	374	20
208	2024-11-06	2024-11-13	2812.95	136	192	4
209	2024-10-26	2024-11-05	2155.90	69	302	5
210	2025-02-27	2025-03-09	3413.20	279	42	14
211	2024-10-01	2024-10-04	1216.08	214	313	10
212	2024-11-03	2024-11-10	3467.24	132	366	2
213	2024-12-25	2024-12-26	280.42	260	161	2
214	2025-02-06	2025-02-07	121.18	333	141	12
215	2025-03-11	2025-03-21	4412.50	310	241	15
216	2024-07-20	2024-07-24	1097.48	53	175	20
217	2025-03-16	2025-03-26	1521.60	59	251	7
218	2025-01-19	2025-01-21	771.16	287	70	6
219	2024-06-22	2024-07-02	2663.90	187	399	10
220	2024-07-30	2024-08-01	803.52	133	125	11
221	2024-06-15	2024-06-22	1326.22	380	220	2
222	2024-04-30	2024-05-05	1561.10	179	180	12
223	2025-02-26	2025-03-08	4087.10	92	108	2
224	2024-11-04	2024-11-11	2231.25	318	340	16
225	2024-05-16	2024-05-26	1221.70	255	294	22
226	2025-03-12	2025-03-13	233.74	16	35	23
227	2025-03-15	2025-03-20	838.75	148	91	22
228	2024-08-12	2024-08-20	3130.88	377	201	4
229	2025-03-02	2025-03-08	2343.36	277	336	9
230	2025-02-13	2025-02-16	812.79	294	345	20
231	2025-03-03	2025-03-07	1771.20	67	123	4
232	2025-01-23	2025-01-30	2159.71	213	144	5
233	2025-02-12	2025-02-13	221.35	38	156	18
234	2024-05-02	2024-05-05	649.77	25	147	1
235	2024-07-09	2024-07-16	2923.55	371	351	18
236	2024-08-16	2024-08-24	1415.20	401	236	12
237	2024-07-11	2024-07-19	2892.32	138	314	3
238	2024-08-29	2024-09-05	3033.45	42	142	17
239	2024-11-20	2024-11-23	455.55	267	84	6
240	2024-05-15	2024-05-24	3290.58	46	202	15
241	2024-11-18	2024-11-25	3404.80	315	384	23
242	2024-04-22	2024-04-23	345.59	270	393	2
243	2024-07-17	2024-07-23	1441.32	130	68	17
244	2024-10-05	2024-10-15	4795.60	189	347	7
245	2024-10-18	2024-10-24	1318.62	180	105	15
246	2024-07-13	2024-07-14	100.54	399	157	15
247	2024-12-02	2024-12-10	3096.96	250	310	18
248	2024-07-24	2024-07-31	3151.54	47	344	2
249	2024-11-15	2024-11-24	1125.54	367	383	16
250	2025-02-23	2025-03-02	3465.07	248	325	8
251	2025-03-12	2025-03-18	2899.02	366	28	11
252	2024-10-30	2024-11-09	3933.60	88	367	16
253	2025-02-07	2025-02-11	1759.80	393	74	12
254	2024-05-15	2024-05-22	3394.16	17	163	12
255	2024-09-29	2024-10-09	3096.30	338	240	4
256	2024-06-26	2024-06-27	149.16	54	193	17
257	2025-03-20	2025-03-26	2436.00	251	89	13
258	2024-12-06	2024-12-16	3947.20	247	293	15
259	2024-09-01	2024-09-08	2304.68	113	203	16
260	2024-10-05	2024-10-10	1965.50	285	208	11
261	2024-11-29	2024-12-03	431.52	225	286	16
262	2024-03-30	2024-04-06	2754.78	49	82	15
263	2024-06-25	2024-07-01	2391.90	269	248	15
264	2024-09-26	2024-10-02	2499.54	397	224	15
265	2024-05-19	2024-05-28	1520.01	209	182	20
266	2024-06-19	2024-06-23	689.56	13	34	16
267	2024-12-19	2024-12-26	1734.81	175	327	5
268	2024-09-09	2024-09-14	1441.80	123	320	1
269	2024-11-09	2024-11-16	1469.09	390	135	13
270	2024-11-21	2024-12-01	1605.50	21	46	18
271	2024-10-27	2024-10-31	1743.44	43	117	8
272	2024-08-23	2024-08-30	1093.68	360	362	10
273	2024-10-11	2024-10-13	268.54	283	356	15
274	2024-05-12	2024-05-19	3444.77	226	375	2
275	2025-03-19	2025-03-25	2182.68	65	324	12
276	2024-10-15	2024-10-16	136.99	26	139	12
277	2024-10-19	2024-10-24	677.15	39	158	13
278	2024-07-03	2024-07-07	1313.28	63	126	12
279	2024-11-15	2024-11-19	475.12	243	124	21
280	2024-04-25	2024-05-05	1320.50	350	95	16
281	2024-04-25	2024-05-02	2605.40	160	263	6
282	2024-10-31	2024-11-04	1601.84	153	185	3
283	2025-03-05	2025-03-11	891.60	145	162	1
284	2024-06-28	2024-06-29	194.24	95	178	6
285	2025-02-01	2025-02-08	2395.19	110	298	11
286	2024-04-22	2024-04-29	2837.52	235	121	22
287	2024-08-03	2024-08-07	642.96	118	90	15
288	2024-04-16	2024-04-17	246.63	217	253	5
289	2024-09-22	2024-09-27	2319.80	51	371	1
290	2025-03-01	2025-03-02	300.00	29	3	8
291	2024-10-08	2024-10-14	767.88	152	262	20
292	2025-02-19	2025-02-27	3631.52	45	51	10
293	2024-12-04	2024-12-10	2125.92	211	77	17
294	2024-08-31	2024-09-10	3477.20	184	59	4
295	2024-04-11	2024-04-18	1394.47	308	275	16
296	2024-04-29	2024-05-03	1065.88	384	237	11
297	2025-01-06	2025-01-07	388.20	195	265	8
298	2024-09-15	2024-09-24	3449.43	71	368	1
299	2024-10-13	2024-10-15	557.50	328	379	16
300	2024-10-09	2024-10-19	4184.30	32	48	22
301	2025-01-06	2025-01-10	1850.92	100	61	9
302	2024-04-13	2024-04-22	1316.52	282	307	12
303	2024-07-21	2024-07-22	340.34	296	146	10
304	2025-02-17	2025-02-25	1391.60	98	80	2
305	2024-06-20	2024-06-29	4334.13	107	291	22
306	2024-12-09	2024-12-12	450.75	373	174	11
307	2024-08-10	2024-08-13	865.11	389	37	12
308	2025-02-16	2025-02-25	1670.49	91	273	8
309	2024-10-05	2024-10-08	1229.91	284	179	21
310	2024-12-09	2024-12-10	323.21	81	76	19
311	2024-12-28	2025-01-05	1949.44	176	73	21
312	2025-01-11	2025-01-20	2900.16	392	277	4
313	2024-08-19	2024-08-27	2028.24	72	382	17
314	2024-09-27	2024-09-30	739.71	286	205	17
315	2024-06-06	2024-06-08	930.84	131	290	5
316	2024-11-13	2024-11-16	536.40	395	189	12
317	2024-06-24	2024-06-28	902.44	264	25	13
318	2024-08-15	2024-08-21	1522.38	220	16	16
319	2024-04-24	2024-05-03	1705.14	349	188	1
320	2025-03-02	2025-03-06	1900.64	227	87	15
321	2024-07-20	2024-07-25	1938.00	143	329	7
322	2024-12-06	2024-12-08	478.72	400	8	16
323	2024-09-22	2024-09-30	3572.88	261	85	10
324	2024-06-08	2024-06-14	650.46	190	159	23
325	2024-03-27	2024-03-29	986.28	307	94	20
326	2025-02-28	2025-03-09	4095.81	253	66	16
327	2025-01-27	2025-01-30	753.69	87	244	4
328	2024-05-20	2024-05-22	435.88	70	30	5
329	2025-03-20	2025-03-30	1803.60	263	65	8
330	2024-08-17	2024-08-25	2990.80	332	132	8
331	2024-12-29	2025-01-06	2618.16	172	228	17
332	2025-02-13	2025-02-21	2024.08	196	198	22
333	2024-06-26	2024-06-29	641.10	276	196	17
334	2025-02-01	2025-02-05	1470.52	320	9	6
335	2024-05-23	2024-05-24	472.39	24	259	10
336	2025-01-08	2025-01-16	1620.00	242	170	22
337	2024-12-30	2025-01-09	1287.50	144	292	7
338	2025-01-19	2025-01-22	1289.43	84	7	8
339	2024-05-28	2024-06-03	1305.00	364	131	12
340	2024-04-06	2024-04-08	905.50	345	235	10
341	2024-12-19	2024-12-28	2552.85	199	365	11
342	2025-01-12	2025-01-22	1937.70	114	389	8
343	2024-03-31	2024-04-05	781.15	34	173	4
344	2024-06-29	2024-06-30	252.96	99	380	18
345	2024-04-02	2024-04-06	1071.40	164	355	22
346	2024-12-23	2024-12-25	307.22	292	377	7
347	2024-08-27	2024-08-30	376.62	203	176	21
348	2024-07-11	2024-07-15	793.08	304	44	2
349	2024-05-15	2024-05-20	650.00	252	1	18
350	2024-10-19	2024-10-21	588.16	171	127	14
351	2025-01-28	2025-01-29	130.98	170	31	13
352	2024-08-24	2024-08-26	705.74	266	118	8
353	2025-03-10	2025-03-15	970.45	291	4	9
354	2024-11-18	2024-11-28	2392.00	106	297	3
355	2024-10-27	2024-10-29	281.52	301	227	18
356	2025-03-02	2025-03-09	1969.17	207	349	3
357	2025-02-21	2025-02-22	142.47	374	155	15
358	2025-02-17	2025-02-20	589.17	396	151	5
359	2024-08-07	2024-08-14	1416.24	280	40	16
360	2025-03-13	2025-03-23	2528.30	210	221	14
361	2024-05-24	2024-05-31	2633.05	117	27	9
362	2025-01-04	2025-01-12	1151.20	241	200	15
363	2025-01-11	2025-01-12	369.69	347	397	21
364	2025-02-03	2025-02-13	3111.70	2	164	23
365	2024-06-15	2024-06-25	1341.00	93	72	13
366	2025-01-06	2025-01-14	1712.80	109	232	8
367	2024-12-18	2024-12-22	1344.44	245	391	19
368	2024-04-19	2024-04-27	3387.36	385	233	17
369	2024-07-30	2024-08-02	1153.71	212	120	2
370	2024-09-25	2024-09-28	1216.62	158	283	7
371	2024-12-19	2024-12-22	1401.24	165	98	16
372	2024-06-01	2024-06-10	2559.15	351	138	18
373	2024-07-12	2024-07-17	527.70	10	238	12
374	2025-02-07	2025-02-16	2986.83	57	184	16
375	2024-07-05	2024-07-11	2916.00	192	401	2
376	2024-05-27	2024-05-28	420.35	249	385	7
377	2025-01-31	2025-02-03	314.58	343	392	5
378	2024-07-20	2024-07-26	1191.30	9	168	4
379	2024-11-20	2024-11-30	4881.60	295	133	9
380	2025-01-18	2025-01-20	928.36	228	319	15
381	2024-05-29	2024-05-31	623.06	365	305	21
382	2024-06-19	2024-06-26	1278.48	182	287	3
383	2024-06-21	2024-07-01	1407.70	97	114	22
384	2024-08-27	2024-09-02	1902.42	194	260	16
385	2025-01-29	2025-02-07	2507.76	229	79	10
386	2024-07-31	2024-08-05	1885.20	297	150	2
387	2024-08-31	2024-09-05	1698.20	272	53	7
388	2024-07-02	2024-07-04	656.98	219	191	21
389	2024-07-23	2024-07-29	1472.70	334	11	6
390	2025-03-20	2025-03-25	1470.75	356	254	2
391	2024-09-27	2024-10-07	4497.90	62	257	23
392	2024-12-27	2024-12-28	125.58	193	153	10
393	2024-11-25	2024-12-04	2745.09	262	112	21
394	2025-01-29	2025-02-04	2649.78	22	226	16
395	2024-10-10	2024-10-19	1174.77	68	312	14
396	2024-12-06	2024-12-09	526.68	290	86	11
397	2024-11-24	2024-11-26	653.50	121	43	6
398	2024-04-09	2024-04-13	1243.88	363	165	9
399	2024-08-10	2024-08-12	795.50	223	137	12
400	2024-09-03	2024-09-08	1335.05	259	318	4
401	2024-08-24	2024-08-28	870.20	177	55	7
402	2025-03-03	2025-03-07	438.40	281	172	15
403	2024-05-07	2024-05-16	2544.39	268	258	2
1	2025-03-10	2025-03-13	390.00	1	2	1
2	2025-03-15	2025-03-16	150.00	2	1	2
3	2025-03-20	2025-03-22	600.00	3	3	3
\.


--
-- Name: branch branch_pkey; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.branch
    ADD CONSTRAINT branch_pkey PRIMARY KEY (branchid);


--
-- Name: car car_licenseplate_key; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_licenseplate_key UNIQUE (licenseplate);


--
-- Name: car car_pkey; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_pkey PRIMARY KEY (carid);


--
-- Name: customer customer_licensenumber_key; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_licensenumber_key UNIQUE (licensenumber);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customerid);


--
-- Name: maintenance maintenance_pkey; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.maintenance
    ADD CONSTRAINT maintenance_pkey PRIMARY KEY (maintenanceid);


--
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (paymentid);


--
-- Name: rental rental_pkey; Type: CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.rental
    ADD CONSTRAINT rental_pkey PRIMARY KEY (rentalid);


--
-- Name: car car_branchid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_branchid_fkey FOREIGN KEY (branchid) REFERENCES public.branch(branchid);


--
-- Name: maintenance maintenance_carid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.maintenance
    ADD CONSTRAINT maintenance_carid_fkey FOREIGN KEY (carid) REFERENCES public.car(carid);


--
-- Name: rental rental_carid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.rental
    ADD CONSTRAINT rental_carid_fkey FOREIGN KEY (carid) REFERENCES public.car(carid);


--
-- Name: rental rental_customerid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.rental
    ADD CONSTRAINT rental_customerid_fkey FOREIGN KEY (customerid) REFERENCES public.customer(customerid);


--
-- Name: rental rental_paymentid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: shira
--

ALTER TABLE ONLY public.rental
    ADD CONSTRAINT rental_paymentid_fkey FOREIGN KEY (paymentid) REFERENCES public.payment(paymentid);


--
-- PostgreSQL database dump complete
--

