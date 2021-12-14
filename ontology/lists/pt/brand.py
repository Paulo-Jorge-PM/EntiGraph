#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#NOTE: DELETED THE ORIGINAL 7000 Brands (too many not common ones) and pasted only the top 500 in Forbes + 132 portuguese brands and companies

data = {
"Apple":"",
"Amazon":"",
"Google":"",
"Microsoft":"",
"Samsung Group":"",
"Walmart":"",
"Facebook":"",
"ICBC":"",
"Verizon":"",
"WeChat":"",
"China Construction Bank":"",
"Toyota":"",
"Mercedes-Benz":"",
"Tencent":"",
"Huawei":"",
"State Grid":"",
"Ping An":"",
"Taobao":"",
"Agricultural Bank Of China":"",
"Home Depot":"",
"AT&T":"",
"Disney":"",
"Deutsche Telekom":"",
"Tmall":"",
"Bank of China":"",
"Volkswagen":"",
"Moutai":"",
"Shell":"",
"BMW":"",
"Alibaba.com":"",
"Starbucks":"",
"China Mobile":"",
"Saudi Aramco":"",
"Mitsubishi Group":"",
"Marlboro":"",
"Porsche":"",
"NTT Group":"",
"McDonald's":"",
"Coca-Cola":"",
"Bank of America":"",
"Citi":"",
"Tesla":"",
"Intel":"",
"Wells Fargo":"",
"PetroChina":"",
"Honda":"",
"Nike":"",
"CSCEC":"",
"Lowe's":"",
"UPS":"",
"Costco":"",
"Chase":"",
"IBM":"",
"UnitedHealthcare":"",
"CVS":"",
"Deloitte":"",
"VISA":"",
"Sinopec":"",
"Oracle":"",
"accenture":"",
"Wuliangye":"",
"Xfinity":"",
"Instagram":"",
"Netflix":"",
"Sumitomo Group":"",
"JP Morgan":"",
"American Express":"",
"JD.com":"",
"FedEx":"",
"Hyundai Group":"",
"Ford":"",
"China Life":"",
"Mitsui":"",
"PWC":"",
"Spectrum":"",
"BP":"",
"TATA Group":"",
"SK Group":"",
"China Merchants Bank":"",
"Target":"",
"Siemens Group":"",
"Uber":"",
"EY":"",
"Allianz":"",
"Evergrande":"",
"Cisco":"",
"Country Garden":"",
"Nestle":"",
"Vodafone":"",
"Mastercard":"",
"Orange":"",
"LG Group":"",
"Dell Technologies":"",
"Bosch":"",
"Pepsi":"",
"Total":"",
"General Electric":"",
"SAP":"",
"IKEA":"",
"Volvo":"",
"AXA":"",
"YouTube":"",
"Audi":"",
"Vanke":"",
"HSBC":"",
"PayPal":"",
"Nissan":"",
"Walgreens":"",
"Hitachi":"",
"TD":"",
"Chevron":"",
"CRCC":"",
"Anthem":"",
"RBC":"",
"Sony":"",
"Bank of Communications":"",
"GUCCI":"",
"Aldi":"",
"CPIC":"",
"KFC":"",
"Shanghai Pudong Development Bank":"",
"CRECG":"",
"Louis Vuitton":"",
"au":"",
"China CITIC Bank":"",
"Adidas":"",
"Santander":"",
"AIA":"",
"NetEase":"",
"Goldman Sachs":"",
"Chevrolet":"",
"Boeing":"",
"Postal Savings Bank":"",
"ExxonMobil":"",
"Humana":"",
"China Telecom":"",
"Chanel":"",
"Salesforce":"",
"ZARA":"",
"UNIQLO":"",
"Capital One":"",
"SoftBank":"",
"China Minsheng Bank":"",
"Optum":"",
"BNP Paribas":"",
"H&M":"",
"TSMC":"",
"KPMG":"",
"MUFG":"",
"Industrial Bank":"",
"Cartier":"",
"Petronas":"",
"Enel":"",
"JR":"",
"Adobe":"",
"Hermès":"",
"Universal":"",
"Lidl":"",
"Greenland":"",
"Longfor Properties":"",
"GEICO":"",
"Sam's Club":"",
"ADNOC":"",
"Johnson & Johnson":"",
"Lockheed Martin":"",
"China Everbright Bank":"",
"L'Oréal":"",
"Warner Bros":"",
"Tesco":"",
"ING":"",
"Renault":"",
"Sephora":"",
"Panasonic":"",
"Midea":"",
"China Resources Land":"",
"Dollar General":"",
"Yili":"",
"DHL":"",
"Morgan Stanley":"",
"Sber":"",
"Nokia":"",
"Engie":"",
"Yahoo! Group":"",
"Xiaomi":"",
"Medtronic":"",
"China Overseas Land & Invest":"",
"EDF":"",
"Ferrari":"",
"stc":"",
"Purina":"",
"Airbus":"",
"7-Eleven":"",
"Poly Real Estate":"",
"BMO":"",
"Scotiabank":"",
"Barclays":"",
"Sky":"",
"Woolworths":"",
"Progressive":"",
"Equinor":"",
"Lexus":"",
"PICC":"",
"Japan Post Holdings":"",
"S&P Global":"",
"UBS":"",
"LIC":"",
"Gree":"",
"Etisalat":"",
"Eni":"",
"NBC":"",
"HP":"",
"Infosys":"",
"U.S. Bank":"",
"eBay":"",
"Metlife":"",
"Brookfield":"",
"Power China":"",
"LinkedIn":"",
"E.Leclerc":"",
"booking.com":"",
"Canon":"",
"Danone":"",
"Carrefour":"",
"Subway":"",
"Subaru":"",
"Red Bull":"",
"Reliance":"",
"ESPN":"",
"Nvidia":"",
"Publix":"",
"Cognizant":"",
"Truist":"",
"3M":"",
"HCA":"",
"Vinci":"",
"Travelers":"",
"Rolex":"",
"China Unicom":"",
"Caterpillar":"",
"John Deere":"",
"Movistar":"",
"Dior":"",
"Haier":"",
"DBS":"",
"Baidu":"",
"Rakuten":"",
"Zurich":"",
"Roche":"",
"Marubeni":"",
"BBVA":"",
"Fox":"",
"BNSF":"",
"Hilton":"",
"Generali Group":"",
"Rabobank":"",
"Gillette":"",
"Union Pacific":"",
"Philips":"",
"Sunac":"",
"Intesa Sanpaolo":"",
"BASF":"",
"Chubb":"",
"Bell":"",
"Merrill":"",
"Meituan":"",
"Canada Life":"",
"Pall Mall":"",
"Yanghe":"",
"CNBM":"",
"SF Express":"",
"Luzhou Laojiao":"",
"Northrop Grumman":"",
"Cigna":"",
"Telenor":"",
"CIBC":"",
"Land Rover":"",
"L&M":"",
"Allstate":"",
"Michelin":"",
"VMWARE":"",
"Aviva":"",
"Telstra":"",
"Nippon Life Insurance":"",
"Sherwin-Williams":"",
"Bridgestone":"",
"PNC":"",
"CNOOC":"",
"Pampers":"",
"CRRC":"",
"Capgemini":"",
"Playstation":"",
"Enterprise":"",
"Kellogg's":"",
"HDFC Bank":"",
"Aetna":"",
"Lay's":"",
"Commonwealth Bank":"",
"Broadcom":"",
"TJ Maxx":"",
"Asda":"",
"Mizuho Financial Group":"",
"Kroger":"",
"Gazprom":"",
"Daiwa House":"",
"Honeywell":"",
"Activision Blizzard":"",
"Tyson":"",
"MCC":"",
"Credit Suisse":"",
"Telus":"",
"Thermo Fisher Scientific":"",
"Best Buy":"",
"Youku":"",
"Raytheon Technologies":"",
"Poste Italiane":"",
"Nivea":"",
"Fubon Financial":"",
"Hikvision":"",
"El Corte Inglés":"",
"QNB":"",
"Domino's Pizza":"",
"Airtel":"",
"20th Television":"",
"Viettel":"",
"Standard Chartered":"",
"TIM":"",
"KEPCO":"",
"Nescafé":"",
"Bouygues":"",
"Circle K":"",
"CBS":"",
"ABC":"",
"State Bank of India":"",
"Corona":"",
"Qualcomm":"",
"Taco Bell":"",
"Delta":"",
"BT":"",
"Valero":"",
"Dunkin":"",
"Guerlain":"",
"Estée Lauder":"",
"Heineken":"",
"FIS":"",
"AutoZone":"",
"Coles":"",
"HPE":"",
"BAE Systems":"",
"Spotify":"",
"Discover":"",
"Pemex":"",
"HCL":"",
"Fresenius":"",
"O2":"",
"Jeep":"",
"Nintendo":"",
"China Post":"",
"Xbox":"",
"Lukoil":"",
"Whole Foods":"",
"Tiffany & Co.":"",
"CFLD":"",
"SFR":"",
"CJ Group":"",
"Lego":"",
"Unicharm Corp":"",
"Mahindra Group":"",
"Munich Re":"",
"Suning":"",
"Tokio Marine":"",
"American Airlines":"",
"Lenovo":"",
"CCCC":"",
"Chow Tai Fook":"",
"Swisscom":"",
"PTT":"",
"Pantene":"",
"Kia":"",
"McKinsey":"",
"Carmax":"",
"Iberdrola":"",
"Pizza Hut":"",
"Manulife":"",
"Dove":"",
"Société Générale":"",
"Itaú":"",
"Hua Xia Bank":"",
"Crédit Mutuel":"",
"ADP":"",
"Wrigley":"",
"Shinhan Financial Group":"",
"Sysco":"",
"General Dynamics":"",
"Clinique":"",
"United Airlines":"",
"Prudential (US)":"",
"BHP":"",
"AbbVie":"",
"Applied Materials":"",
"McKesson":"",
"Lloyds Bank":"",
"Centene Corporation":"",
"Swiss Re":"",
"Monster":"",
"Crédit Agricole":"",
"NatWest":"",
"Jio":"",
"Budweiser":"",
"Mengniu":"",
"Mercadona":"",
"Centurylink":"",
"E.ON":"",
"ABB":"",
"Zalando":"",
"COACH":"",
"Micron Technology":"",
"Hyatt":"",
"KB Financial Group":"",
"Rogers":"",
"Emirates":"",
"Claro":"",
"Danaher":"",
"The North Face":"",
"Express Scripts":"",
"ANZ":"",
"Daikin":"",
"Texas Instruments":"",
"Conch":"",
"Ross Dress For Less":"",
"OCBC Bank":"",
"Tide":"",
"BD":"",
"Geely":"",
"AIG":"",
"Haidilao":"",
"BUICK":"",
"Sprite":"",
"Bloomberg":"",
"New China Life (NCL)":"",
"Saint-Gobain":"",
"Bayer":"",
"McLane":"",
"SiriusXM":"",
"Cardinal Health":"",
"Marshalls":"",
"BOE":"",
"Electronic Arts":"",
"Telia":"",
"Indian Oil":"",
"BNY Mellon":"",
"AmerisourceBergen":"",
"Aflac":"",
"Safran":"",
"LENNAR":"",
"Servicenow":"",
"Wipro":"",
"GS Group":"",
"Blackrock":"",
"McCain":"",
"Sodexo":"",
"Yonghui Superstores":"",
"CNP Assurances":"",
"China Re":"",
"Cadillac":"",
"China Taiping":"",
"Anta":"",
"Logan":"",
"Emerson Electric":"",
"Gatorade":"",
"Victoria's Secret":"",
"La Poste":"",
"Bristol-Myers Squibb":"",
"Sainsbury's":"",
"BDO Global":"",
"Merck & Co":"",
"ASML":"",
"Nordea":"",
"Garnier":"",
"Canadian National Railway":"",
"Huggies":"",
"D.R. Horton":"",
"Fujitsu Group":"",
"Abbott":"",
"Tim Hortons":"",
"Maersk":"",
"Gujing Gong Jiu":"",
"HBO":"",
"Bank of Beijing":"",
"Cummins":"",
"Omega":"",
"Banco do Brasil":"",
"Victoria":"",
"Pfizer":"",
"SABIC":"",
"Head & Shoulders":"",
"Sompo Japan Nipponkoa":"",
"UOB":"",
"Edeka":"",
"MSCI":"",
"Altri ":"",
"Ambar – Ideas on Paper S.A. ":"",
"Banco Comercial Português ":"",
"Bial ":"",
"Caixa Geral de Depósitos ":"",
"Carris ":"",
"Central de Cervejas ":"",
"Chipidea ":"",
"Churchill's Port ":"",
"Ciberbit ":"",
"Cimpor ":"",
"CMS-Helmets ":"",
"Cofina ":"",
"Conservas Ramirez ":"",
"Continente ":"",
"Corticeira Amorim ":"",
"Critical Software ":"",
"CTT":"",
"Delta Cafés ":"",
"EFACEC ":"",
"EDP":"",
"Fábrica Nacional de Munições de Armas Ligeiras ":"",
"Galp Energia ":"",
"Glintt ":"",
"Grupo José de Mello ":"",
"Iberomoldes ":"",
"Impresa ":"",
"Jerónimo Martins ":"",
"Lactogal ":"",
"Logoplaste ":"",
"Martifer ":"",
"Media Capital ":"",
"Medinfar ":"",
"MEO ":"",
"Montepio ":"",
"Mota-Engil ":"",
"Move Interactive ":"",
"NOS ":"",
"Novabase ":"",
"Novo Banco ":"",
"Pingo Doce ":"",
"Porto Editora ":"",
"Portugal Telecom ":"",
"Quidgest ":"",
"RTP":"",
"REN":"",
"Renova ":"",
"SAPO ":"",
"Semapa ":"",
"Simoldes ":"",
"Soares da Costa ":"",
"SIC":"",
"Sonae ":"",
"Sovena Group ":"",
"Sumol":"",
"Compal ":"",
"Tabaqueira ":"",
"TAP ":"",
"The Navigator Company ":"",
"Tranquilidade ":"",
"Tupam editores ":"",
"UMM ":"",
"Unicer Brewery ":"",
"Uniplaces ":"",
"Visabeira ":"",
"Vista Alegre":"",
"Ach. Brito":"",
"Active Space Technologies":"",
"Sevenair Air Services":"",
"AJP Motos":"",
"Altice Portugal":"",
"Aptoide":"",
"Azores Airlines":"",
"Baboom":"",
"Portuguese Commercial Bank":"",
"Bluepharma":"",
"BRM Costruções Aeronáuticas":"",
"Casa Batalha":"",
"Cerâmica de Valadares":"",
"Cimpor":"",
"CMS-Helmets":"",
"Cockburn's Port House":"",
"Comboios de Portugal":"",
"Crioestaminal":"",
"Esmaltina":"",
"EuroAtlantic Airways":"",
"Fonseca Guimaraens":"",
"Foreva":"",
"Galp Energia":"",
"Glintt":"",
"Gilberto Grácio":"",
"Graham's":"",
"Hovione":"",
"Iberomoldes":"",
"José Maria da Fonseca":"",
"Karta GPS":"",
"Lactogal":"",
"Laranjada":"",
"Majora":"",
"Martifer":"",
"Mateus":"",
"Maxdata Software":"",
"Medinfar":"",
"NDrive":"",
"Nelo":"",
"Novabase":"",
"OGMA":"",
"Omni Aviation":"",
"Onda":"",
"Órbita bicycles":"",
"Parfois":"",
"Partex":"",
"Pestana Group":"",
"Porches Pottery":"",
"Sandeman":"",
"Portugália Airlines":"",
"Portuscale Cruises":"",
"Reguladora":"",
"Vinci":"",
"Revigrés":"",
"Sagres":"",
"Salvador Caetano":"",
"Super Bock":"",
"Taylor, Fladgate, & Yeatman":"",
"Temahome":"",
"Tomé Fèteira":"",
"Um Bongo":"",
"Viarco":"",
"Visabeira":"",
"Vitesse Models":"",
"White Airways":"",
"Zippy Kidstore":"",
}