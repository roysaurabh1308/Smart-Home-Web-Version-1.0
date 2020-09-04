import pyrebase
import urllib.request
import datetime

def stream_handler(message):
    # print(message["event"]) # put
    # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    # print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    datadict=db.child("smarthome").get().val()
    datalist=[str(datadict[x]) for x in datadict]
    
    #part2
    fp = urllib.request.urlopen("https://tools.keycdn.com/geo")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    lines=mystr.split("\n")
    city={'Carnicobar':'43367','Maya Bandar':'43309','Nancowrie':'43382','Port Blair':'43333','Amravati':'99961','Anantapur':'43237','Cuddappah':'43241','Gannavaram':'99988','Hakimpet IAF':'99933','Hayathnagar':'99932','Icrisat Patancheru':'99934','Kakinada':'43189','Kalingapatnam':'43105','Kurnool':'43213','Machilipatnam':'43185','Nellore':'43245','Ongole':'43221','Rajinder Nagar':'99931','Tirupathi':'43275','Vijayawada':'43181','Visakhapatnam':'43149','Anni':'30002','Itanagar':'42308','Passighat':'42220','Tawang':'30001','Barpeta':'40001','Dhubri':'42406','Dibrugarh':'42314','Dispur':'99979','Goalpara':'42407','Golaghat':'42420','Guwahati':'42410','IIT Guwahati':'99987','Jorhat':'42423','Lumding':'42523','Mazbat':'42413','North Lakhimpur':'42309','Silchar':'42619','Tezpur':'42415','Tinsukia':'42317','Aurangabad':'50003','Bhagalpur':'42498','Chapra':'42488','Farbesganj':'42395','Gaya':'42591','Madhubani':'50001','Motihari':'42383','Muzaffarpur':'42387','Nalanda':'50002','Patna':'42492','Patna City':'99986','Purnea':'42500','Rajgir':'50004','Supaul':'42393','Ambikapur':'42693','Bilaspur':'60002','Durg':'42876','Jagdalpur':'43041','Janjgir':'60001','Labhandi':'99974','Pendra':'42779','Raipur':'42874','Rajnandgaon':'42948','Ayanagar':'42180','Delhi University':'99921','Narela':'99922','Palam':'42181','Ridge':'42184','Safdarjung':'42182','Diu':'42914','Mapusa':'99984','Old Goa':'99985','Panjim':'43192','Pernem':'99983','Ahmedabad':'42647','Ahmedabad Airport':'99935','Ambli-Bopal':'99956','Amreli':'42834','Baroda':'42748','Bhavnagar':'42838','Bhuj':'42634','Chandkheda':'99938','Dadra Nagar Haveli':'99964','Deesa':'42539','Dwarka':'42731','Gift City, Gandhi Nagar':'99960','Idar':'42651','IIPH,Gandhi Nagar':'99959','Kandla':'42638','Naliya':'42631','Navrangpura (S.P.Stadium)':'99936','Okha':'42730','Pirana':'99958','Porbandar':'42830','Raikhad':'99957','Rajkot':'42737','Rakhiyal':'99937','Satellite Area (ISRO-SAC)':'99939','Surat':'42840','Veraval':'42909','Ambala':'42103','Bhiwani':'42350','ndigarh':'10" t','Chandigarh Airport':'99928','Faridabad':'10001','Gurgaon':'42178','Hisar':'42131','Karnal':'42137','Kurukshetra':'99915','Mohali':'99930','Narnaul':'42177','Panchkula':'99929','Rohtak':'42176','Sirsa':'99916','Bilaspur':'42080','hamba':'8205"','Dharamsala':'42062','Hamirpur':'11001','Kalpa':'42066','Keylong':'42063','Kullu':'42081','Manali':'42065','Nahan':'42104','Shimla':'42083','Solan':'42106','Sundernagar':'42079','Una':'42077','Banihal':'42045','Batote':'42043','Bhaderwah':'42048','Dal Lake':'99976','Gulmarg':'42026','Jammu':'42056','Jammu Airport':'99981','Katra':'42054','Kukernag':'42046','Kupwara':'42031','Leh':'42034','Mata Vaishno Devi ji':'99980','Pahalgam':'42028','Qazigund':'42044','Srinagar':'42027','Srinagar Airport':'99975','Bokaro':'13001','Chaibasa':'42795','Daltonganj':'42587','Deogarh':'13002','Dumka':'42599','Giridih':'13003','Jamshedpur':'42798','Kanke':'99950','Ranchi':'42701','Agumbe':'43257','Ballari':'43205','Belagavi':'43198','Bengaluru ':'43295','Bengaluru International Airport':'99962','Chitradurga':'43233','Gadag':'43201','GKVK':'99963','Hassan':'43263','Honnavar':'43226','Kalaburgi':'43121','Karwar':'43225','Madikeri':'43287','Mandya':'43289','Mangaluru':'43284','Mysuru':'43291','Raichur':'43169','Vijayapura':'43161','Alapuzha':'43352','Kannur':'43315','Kochi':'43353','Kottayam':'43355','kozhikode':'43320','Punalur':'43354','Thiruvananthapuram':'43371','Agati':'43312','Amini Divi':'43311','Kavarati':'43337','Minicoy':'43369','Airport':'99977','Betul':'42860','Bhopal':'42667','Dhar':'42752','Guna':'42559','Gwalior':'42361','Indore':'42754','Jabalpur':'42675','Khajuraho':'42567','Khandwa':'42855','Mandla':'42776','Nabi Bagh':'99978','Pachmarhi':'42767','Rewa':'42574','Sagar':'42671','Satna':'42571','Seoni':'42771','Shivpuri':'42459','Ujjain':'42662','Umaria':'42679','Ahmednagar':'43009','Akola city':'42933','Alibag':'43058','Amaravati':'42937','Aurangabad':'43014','Beed':'43011','Buldhana':'42931','Chandrapur':'43029','Colaba':'43057','College of Agriculture':'99982','Dahanu':'43001','Gondia':'42871','Harnai':'43109','Jalgaon':'42851','Jeur':'43071','Kolhapur':'43157','Mahabaleshwar':'43111','Malegaon':'42925','Mumbai-Borivali':'99941','Mumbai-Chembur':'99943','Mumbai-Mulund':'99944','Mumbai-Powai':'99942','Mumbai-Santacruz':'43003','Mumbai-Worli':'99945','Nagpur':'42867','Nanded':'43021','Nasik':'42921','Navi Mumbai (Panvel)':'99940','Osmanabad':'43075','Parbhani':'43017','Pune-Lohegaon Airport':'43064','Pune-Pashan':'43067','Pune-Shivajinagar':'43063','Ratnagiri':'43110','Sangli':'43158','Satara':'43113','Sholapur':'43117','Thane':'18001','Udgir':'43076','Vengurla':'43193','Wardha':'42939','Yeotmal':'42943','Imphal':'42623','Cherrapunji':'42515','Shillong':'42516','Aizwal':'42726','Champhai':'19001','Lengpui':'42727','Dimapur':'21001','Kohima':'42527','Mokokchung':'21002','Angul':'42969','Balasore':'42895','Bhabanipatna':'23001','Bhubneshwar Airport':'42971','Chandbali':'42973','Cuttack':'42970','Dhenkanal':'42881','Gopalpur':'43049','Jharsuguda':'42886','Keonjhargarh':'42891','Koraput':'43097','Orissa University of Agriculture & Technology':'99949','Paradip':'42976','Pulbani':'42966','Puri':'43053','Sambalpur':'42883','Titlagarh':'42961','Pondicherry':'43328','Amritsar':'42071','Anandpur Sahib':'99917','Bhatinda':'42097','ndigarh':'10" t','Chandigarh Airport':'99928','Ferozepore':'42096','Jalandhar':'42075','Kapurthala':'42074','Ludhiana':'42099','Mohali':'99930','Pathankot':'42057','Patiala':'42101','Ajmer':'42343','Alwar':'42255','Amer':'99969','Banswada':'42655','Barmer':'42435','Bharatpur':'42258','Bhilwara':'42447','Bikaner':'42165','Bundi':'42450','Chittorgarh':'42546','Churu':'42170','Collectorate Circle':'99968','Dholpur':'42354','Hanumangarh':'99919','Jaipur':'42348','Jaisalmer':'42328','Jalore':'42439','Jhalawar':'42555','Jodhpur':'42339','Kota ':'42452','Mount Abu':'42540','Nagaur':'42242','Pali':'99920','Pilani':'42174','Sawai Madhopur':'42453','Siker':'42249','Sriganganagar':'42123','Tonk':'42349','Transport Nagar':'99967','Udaipur ':'42542','Vaishali Nagar':'99966','Gangtok':'42299','Gyalsingh':'26002','Mangan':'26001','Namchi':'26003','Tadong':'42217','Chennai - Meenambakkam':'43279','Coimbatore':'43321','Coonoor':'43318','Dharmapuri':'43301','Ennore':'99948','Kanyakumari':'43377','Karaikal':'43346','Kodaikanal':'43339','Madhavaram':'99947','Madurai ':'43360','Nagapattinam':'43347','Nungambakkam':'43278','Palayankottai':'43376','Pamban':'43363','Salem':'43325','Thiruvallikeni':'99946','Tiruchirapalli':'43344','Tondi':'43361','Vellore':'43303','Hanamkonda':'43087','Hyderabad':'43128','Nizamabad':'43081','Patancheru':'99965','Ramagundam':'43086','Agartala':'42724','Kailashahar':'42618','Agra':'42260','Aligarh':'42262','Allahabad':'42475','Bahraich':'42273','Banda':'42473','Bareilly':'42189','Faizabad':'42374','Fursatganj':'42372','Gorakhpur':'42379','Hardoi':'42271','Jhansi':'42463','Kanpur':'42366','Lucknow':'42369','Lucknow Hanuman Setu':'99970','Luckonw Control Room':'99971','Malihabad':'99972','Meerut':'42139','Mohanlalganj':'99973','Moradabad':'42187','Muzaffarnagar':'30052','Shahjahanpur':'30051','Sultanpur':'42375','Varanasi':'42479','Almora':'99912','Asharori':'99954','Champawat':'31001','Dehradun':'42111','Haridwar':'99918','Joshimath':'42116','Karanpur':'99951','Mukteshwar':'42147','Mussorie':'42112','Nainital':'42146','Pantnagar':'42148','Pithoragarh':'99911','Sahastradhara':'99953','Tehri':'42114','UCOST':'99955','Uttarkashi':'42108','Asansol':'42704','Baharampur':'42603','Bankura':'42707','Burdwan':'42709','Coochbehar':'42403','Darjeeling':'42295','Diamond Harbour':'42811','Digha':'42901','Dum Dum -Kolkata':'42809','Howrah (Uluberia)':'42805','Jalpaiguri':'42399','Kolkata-Alipore':'42807','Krishnanagar':'42711','Malda':'42503','Midnapore':'42803','Salt Lake-Kolkata':'42816','Sriniketan':'42708'}
    cc=lines[238].split("'")[-2]
    #print(city[cc])
    fp = urllib.request.urlopen("http://city.imd.gov.in/citywx/city_weather.php?id="+city[cc])
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    lines=mystr.split("\n")
    max_temp=lines[30][:(len(lines[30])-12)]
    min_temp=lines[46][:(len(lines[46])-12)]
    rain=lines[62][:(len(lines[62])-12)]
    rel_hum1=lines[70][:(len(lines[70])-12)]
    rel_hum2=lines[78][:(len(lines[78])-12)]
    x = datetime.datetime.now()

    datatf=[max_temp,min_temp,rain,rel_hum1,rel_hum2,str(x.hour),str(x.month),str(datalist[2])]
    mdt=",".join(datatf)
    fl=open('data.csv','a')
    fl.write("\n"+mdt)
    fl.close

config={
    "apiKey": "AIzaSyBcXcAtVqPT87iAxDgi9ilV5XhIkMIcdv0",
    "authDomain": "smart-home-1343e.firebaseapp.com",
    "databaseURL": "https://smart-home-1343e.firebaseio.com",
    "projectId": "smart-home-1343e",
    "storageBucket": "smart-home-1343e.appspot.com",
    "messagingSenderId": "228104491397",
    "appId": "1:228104491397:web:3b561ae413e0aa9bf7b4ec",
    "measurementId": "G-NBBEN0BRWF"

}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
#users = db.child("smarthome").get()
my_stream = db.child("smarthome").stream(stream_handler)