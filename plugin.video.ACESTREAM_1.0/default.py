                                             
import xbmc                                     
import xbmcaddon
import xbmcplugin
import plugintools                                                           
import six
import xbmcvfs
myaddon =xbmcaddon .Addon ()

if six.PY2:
   translatePath = xbmc.translatePath
   LOG = xbmc.LOGNOTICE
elif six.PY3:
   translatePath = xbmcvfs.translatePath
   LOG = xbmc.LOGINFO

def run():                                               
   plugintools.log("--->  <---")        
   plugintools.set_view(plugintools.LIST)              
                                                           
                                          
   params = plugintools.get_params()                     
    
   if params.get("action") is None:                      
      main_list(params)                              
   else:                                                
      action = params.get("action")
      exec (action+"(params)")
    
   plugintools.close_item_list()




def main_list(params):

 
  
   
       plugintools.add_item(action = "DAZN" , title = "[COLOR lime][B]DAZN[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/DAZN_logo.png"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/DAZN_logo.png" , plot = "",  folder = True,isPlayable = False  )

 
       plugintools.add_item(action = "DAZN_LaLiga" , title = "[COLOR lime][B]DAZN LaLiga[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/DAZN_LIGA.png"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/DAZN_LIGA.png" , plot = "",  folder = True,isPlayable = False  )
       

       plugintools.add_item(action = "DAZN_liga_femenina" , title = "[COLOR lime][B]DAZN Liga Femenina[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/LIGA_F.jpg"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/LIGA_F.jpg" , plot = "",  folder = True,isPlayable = False  )


       plugintools.add_item(action = "Dazn_f1" , title = "[COLOR lime][B]DAZN F1[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/DAZN_F1.png"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/DAZN_F1.png" , plot = "",  folder = True,isPlayable = False  )


       plugintools.add_item(action = "EuroSport" , title = "[COLOR lime][B]EuroSport[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/logo_eurosport_nuevo.jpg"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/logo_eurosport_nuevo.jpg" , plot = "",  folder = True,isPlayable = False  )


       plugintools.add_item(action = "Movistar_deportes" , title = "[COLOR lime][B]M+ Deportes[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/M_DEPORTES.png"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/M_DEPORTES.png" , plot = "",  folder = True,isPlayable = False  )

       plugintools.add_item(action = "Movistar_liga" , title = "[COLOR lime][B]M+ LaLiga[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/LaLigaTV-por-M_Color-Negativo_RGB.jpg"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/LaLigaTV-por-M_Color-Negativo_RGB.jpg" , plot = "",  folder = True,isPlayable = False  )
       
       plugintools.add_item(action = "Movistar_liga_campeones" , title = "[COLOR lime][B]M+ Liga de Campeones[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/1655281910291.jpg"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/1655281910291.jpg" , plot = "",  folder = True,isPlayable = False  )

       plugintools.add_item(action = "LaLiga_Smartbank" , title = "[COLOR lime][B]LaLiga Smartbank[/B][/COLOR]" , thumbnail = "resources/screenshots/daznf1.png"  , fanart = "resources/screenshots/daznf1.png" , plot = "",  folder = True,isPlayable = False  )
       
       plugintools.add_item(action = "varios" , title = "[COLOR lime][B]VARIOS[/B][/COLOR]" , thumbnail = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/logo-deportes.jpg"  , fanart = "https://raw.githubusercontent.com/PECASCUCO/pecascuco.github.io/main/IMAGENES%20ADDON/logo-deportes.jpg" , plot = "",  folder = True,isPlayable = False  )


def varios(params):
    canales={}
    canales = {"canal01" : {"nombre" : "M+ Plus" ,
                           "id" : "5a236fbbe6e5bbfec03db548c244a7c858d675c0"} ,    
                "canal02" : {"nombre" : "Copa (op1)" ,
                           "id" : "8ba764f6a3bce6eae87ec71208fad1aa3a20528d"} ,     
                "canal03" : {"nombre" : "Copa (op2)" ,
                           "id" : "d6cdd724a97fcf851e7ef641c28d6beb8663496e"} ,
                "canal04" : {"nombre" : "Copa (op3)" ,
                           "id" : "7d70685696722c2b1b48a5ae1a7f92c445d9443d"} ,
                "canal05" : {"nombre" : "#Vamos" ,
                           "id" : "859bb6295b8d0f224224d3063d9db7cdeca03122"} ,
                "canal06" : {"nombre" : "#Ellas" ,
                           "id" : "67654e63b5065cdaa6c8e8d41bb5428b42b32830"} ,
                          "canal07" : {"nombre" : "M+ Golf" ,
                           "id" : "4f945b0ba4206fa2676b61e9eaa465ac3dcc8122"} ,
                           "canal08" : {"nombre" : "M+ Golf 2" ,
                           "id" : "9a4f3ae6563668b7709dac509dedc709441b3fd9"} ,
                           "canal09" : {"nombre" : "GolTV" ,
                           "id" : "d4627f7b6b237a8556819445b3283d866caceca2"} ,
                           "canal10" : {"nombre" : "Tennis channel" ,
                           "id" : "9292d3b32432efb56db4014933cbdec0a7cf2e36"} ,
                           "canal11" : {"nombre" : "Sport Tv 1" ,
                           "id" : "ce235921dac95e1da2dd5e54673c2fecb9e806de"} ,
                           "canal12" : {"nombre" : "Sport Tv 2" ,
                           "id" : "396d82ca6f5445abcd32e6b609d67e332ee12ace"} ,
                           "canal13" : {"nombre" : "Sport Tv 3" ,
                           "id" : "f8cb9d9e3077eb3ae417b2d95a69c5f590760eb9"}} 
    
    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  


def Movistar_liga_campeones(params):
    canales={}
    canales = {"canal01" : {"nombre" : "M. LaLiga Campeones 1080 (op1)" ,
                           "id" : "931b1984badcb821df7b47a66ac0835ac871b51c"} ,    
                "canal02" : {"nombre" : "M. LaLiga Campeones 1080 (op2)" ,
                           "id" : "f096a64dd756a6d549aa7b12ee9acf7eee27e833"} ,     
                "canal03" : {"nombre" : "M. LaLiga Campeones 1080 (op3)" ,
                           "id" : "1d79a7543d691666135669f89f3541f54e2dd0a9"} ,
                "canal04" : {"nombre" : "M. LaLiga Campeones 720" ,
                           "id" : "e2e2aca792aae5da19995ac516b1d620531bd49c"} ,
                "canal05" : {"nombre" : "M. LaLiga Campeones 2 1080" ,
                           "id" : "fc2fe31b0bce25e2dc7ab4d262bf645e2be5a393"} ,
                "canal06" : {"nombre" : "M. LaLiga Campeones 2 720" ,
                           "id" : "6753492c1908274c268a1b28e2a054a0ff8f86f9"} ,
                          "canal07" : {"nombre" : "M. LaLiga Campeones 3" ,
                           "id" : "ad372cba73aa0ece207a79532b3e30b731136bb2"} ,
                           "canal08" : {"nombre" : "M. LaLiga Campeones 4" ,
                           "id" : "f2df4f96b23388b45e75d848a48a510cf8af560f"} ,
                           "canal09" : {"nombre" : "M. LaLiga Campeones 5" ,
                           "id" : "67b353ab1c4c2f6396b3ca5c4b45023bd9927561"} ,
                           "canal10" : {"nombre" : "M. LaLiga Campeones 6" ,
                           "id" : "64a9353032efa2acb093d0bb86481f20f482d47e"} ,
                           "canal11" : {"nombre" : "M. LaLiga Campeones 7" ,
                           "id" : "5932623d2fd7ed16b01787251b418e4f59a01cda"}} 
    
    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  
       
def LaLiga_Smartbank(params):
    canales={}
    canales = {"canal01" : {"nombre" : "LaLiga Smartbank 1080" ,
                           "id" : "4c46585214b23b1d802ef2168060c7649a3894cf"} ,    
                "canal02" : {"nombre" : "LaLiga Smartbank 720" ,
                           "id" : "06b367c22394a1358c9cefa0cb5d0b64b9b2b3f4"} ,     
                "canal03" : {"nombre" : "LaLiga Smartbank 2 1080" ,
                           "id" : "d81b4f2f3fde433539c097b2edc9b587ca47b087"} ,
                "canal04" : {"nombre" : "LaLiga Smartbank 2 720" ,
                           "id" : "2709d0ab86cb6ce7ba4d3ad188d7fa80668f2924"} ,
                "canal05" : {"nombre" : "LaLiga Smartbank 3" ,
                           "id" : "b4a076c1f67a5c1f1ba899ac61b9401b1dc30f41"} ,
                "canal06" : {"nombre" : "LaLiga Smartbank 4" ,
                           "id" : "2cacf21476b036e319bcb7c7e747766e6ccc082e"} ,
                          "canal07" : {"nombre" : "LaLiga Smartbank 5" ,
                           "id" : "a1146358aa50c99c887108b17f62f9264186a16a"} ,
                           "canal08" : {"nombre" : "LaLiga Smartbank 6" ,
                           "id" : "7a9bb1b9cccb759c44ed84f3c1283922e6854670"} ,
                           "canal09" : {"nombre" : "LaLiga Smartbank 7" ,
                           "id" : "446e73a22582921393b020ed08b768ad8e14d754"} ,
                           "canal10" : {"nombre" : "LaLiga Smartbank 8" ,
                           "id" : "4d52fc1994fe927702aeb7bc8778e2f23b1260e2"}} 
    
    for key in canales:
         title = canales[key]['nombre']
         plot = canales[key]['id']
   
         plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  

def Movistar_liga(params):
    canales={}
    canales = {"canal01" : {"nombre" : "M. LaLiga 1080(op1)" ,
                           "id" : "aa82e7d4f03061f2144a2f4be22f2e2210d42280"} ,    
                "canal02" : {"nombre" : "M. LaLiga 1080(op2)" ,
                           "id" : "7d8c87e057be98f00f22e23b23fbf08999e4b02f"} ,     
                "canal03" : {"nombre" : "M. LaLiga 1080(op3)" ,
                           "id" : "1969c27658d4c8333ab2c0670802546121a774a5"} ,
                "canal04" : {"nombre" : "M. LaLiga 720" ,
                           "id" : "f031f5728b32f6089dda28edebe990cf198108d8"} ,
                "canal05" : {"nombre" : "M. LaLiga 2 1080" ,
                           "id" : "26029f72a4ca831d09deefe89534818db1d105bc"} ,
                "canal06" : {"nombre" : "M. LaLiga 2 720" ,
                           "id" : "80126b240f3e4e004754fd8f8103e857ab2556a0"} ,
                          "canal07" : {"nombre" : "M. LaLiga 3" ,
                           "id" : "4c4844564313e39a888f593511f299f5ba3cf929"} ,
                           "canal08" : {"nombre" : "M. LaLiga 4" ,
                           "id" : "aa8f826da70e27a26b29c7b32402f17e8a67a8b0"} ,
                           "canal09" : {"nombre" : "M. LaLiga 5" ,
                           "id" : "535394f62a810bc5aeb25be75ea5ff7d03e070b2"} ,
                           "canal10" : {"nombre" : "M. LaLiga 6" ,
                           "id" : "c896d37778f9e43549a788fc22206a655895b51b"} ,
                           "canal11" : {"nombre" : "M. LaLiga BAR" ,
                           "id" : "aa82e7d4f03061f2144a2f4be22f2e2210d42280"}} 
    
    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  



def DAZN_liga_femenina(params):
    canales={}
    canales = {"canal01" : {"nombre" : "Dazn liga F 1" ,
                           "id" : "600222a4f98df80a2c0df2d60cb5ff3df9620710"} ,    
                "canal02" : {"nombre" : "Dazn liga F 2" ,
                           "id" : "d6cdd724a97fcf851e7ef641c28d6beb8663496e"} ,     
                "canal03" : {"nombre" : "Dazn liga F 3" ,
                           "id" : "162942adc047d0f78eac056effbe5bbec54a5e51"} ,
                "canal04" : {"nombre" : "Dazn liga F 4" ,
                           "id" : "e454681a152a86da504e63694f17f90d0586867d"}} 
    
    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  

def DAZN(params):
    canales={}
    canales = {"canal01" : {"nombre" : "DAZN 1 1080" ,
                           "id" : "8ca07071b39185431f8e940ec98d1add9e561639"} ,    
                "canal02" : {"nombre" : "DAZN 1 720" ,
                           "id" : "eaff9293c76a324c750ef5094c2a4e2c96518d1f"} ,     
                "canal03" : {"nombre" : "DAZN 2 1080" ,
                           "id" : "60dbeeb299ec04bf02bc7426d827547599d3d9fc"} ,
                "canal04" : {"nombre" : "DAZN 2 720" ,
                           "id" : "7aa402bab9fff43258fbcf401881a39475f30aaf"} ,
                "canal05" : {"nombre" : "DAZN 3" ,
                           "id" : "a8ffddef56f082d4bb5c0be0d3d2fdd8c16dbd97"} ,
                "canal06" : {"nombre" : "DAZN 4" ,
                           "id" : "2fcdf7a19c0858f686efdfabd3c8c2b92bf6bcfd"} }

    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  


def DAZN_LaLiga(params):
    canales={}
    canales = {"canal01" : {"nombre" : "DAZN LaLiga 1080(op1)" ,
                           "id" : "1960a9be8ae9e8c755330218eac4c5805466290a"} ,    
                "canal02" : {"nombre" : "DAZN LaLiga 1080(op2)" ,
                           "id" : "75251ba975132ec9a202806ba5bf606e87280c96"} ,     
                "canal03" : {"nombre" : "DAZN LaLiga 720" ,
                           "id" : "a3bca895c58d3fc7d5e4259d3d5e3cf0291d1914"} ,
                "canal04" : {"nombre" : "DAZN LaLiga 2 1080" ,
                           "id" : "e33e666c393ef04ebe99a9b92135d2e0b48c4d10"} ,
                "canal05" : {"nombre" : "DAZN LaLiga 2 720" ,
                           "id" : "02b9307c5c97c86914cc5939d6bbeb5b4ec60b47"} ,
                "canal06" : {"nombre" : "DAZN LaLiga 3" ,
                           "id" : "8c71f0e0a5476e10950fc827f9d2a507340aba74"} ,
                "canal07" : {"nombre" : "DAZN LaLiga 4" ,
                           "id" : "2792a8a5f4a3f53cd72dec377a2639cd12a6973e"} ,
                "canal08" : {"nombre" : "DAZN LaLiga 5" ,
                           "id" : "99e544cddbee13798e854c1009ee7d1a93fdedf7"} }

    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  


def Dazn_f1(params):
   canales={}
   canales = {"canal02" : {"nombre" : "DAZN F1 1080 (op1)" ,
                           "id" : "5789ca155323664edd293b848606688edf803f4d"} ,     
                "canal03" : {"nombre" : "DAZN F1 1080 (op2)" ,
                           "id" : "9dad717d99b29a05672166258a77c25b57713dd5"} ,
                "canal04" : {"nombre" : "DAZN F1 720" ,
                           "id" : "e1fcad9de0c782c157fde6377805c58297ab65c2"} }
   for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  



def Movistar_deportes(params):
  
   canales={}
   canales = {"canal01" : {"nombre" : "M. Deportes 1080" ,
                           "id" : "ad00223931b1854163e24c5c22475015d7d45c112"} ,    
                "canal02" : {"nombre" : "M. Deportes 720" ,
                           "id" : "77d83a79afcf6c865289cd8cdb42223cd4b6501c"} ,     
                "canal03" : {"nombre" : "M. Deportes 2" ,
                           "id" : "e6f06d697f66a8fa606c4d61236c24b0d604d917"} ,
                "canal04" : {"nombre" : "M. Deportes 3" ,
                           "id" : "aee0a595220e0f1c2fee725fd1dbc602d7152a9a"} ,
                "canal05" : {"nombre" : "M. Deportes 4" ,
                           "id" : "42e83c337ece0af9ca7808859f84c7960e9cb6f5"} ,
                "canal06" : {"nombre" : "M. Deportes 5" ,
                           "id" : "b1e5abc48195b7ca9b2ee1b352e790eb9f7292e3"} ,
                "canal07" : {"nombre" : "M. Deportes 6" ,
                           "id" : "8587ed8ac36ac477e1d4176d3159a38bd154d4ce"}}
 
   for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                       
def  EuroSport(params):
    canales={}
    canales = {"canal01" : {"nombre" : " EuroSport 1 1080" ,
                           "id" : "5e4cd48c79f991fcbee2de8b9d30c4b16de3b952"} ,    
                "canal02" : {"nombre" : " EuroSport 2 1080" ,
                           "id" : "c373da9e901d414b7384e671112e64d5a2310c29"}}

    for key in canales:
       title = canales[key]['nombre']
       plot = canales[key]['id']
   
       plugintools.add_item ( action = "resolve_acestream" , title = "[COLOR yellow][B]" + title + "[/B][/COLOR]" , plot = plot, url="", thumbnail = "https://i.imgur.com/pDh2Gmp.jpg"  , fanart = "https://i.imgur.com/pDh2Gmp.jpg" , folder = False , isPlayable = True )
                  


def resolve_acestream ( params ) :
   import resolveurl
   finalurl = "plugin://script.module.horus?action=play&id={}&title={}&iconimage={}".format(params.get("plot"),params.get("title"),params.get("thumbnail"))
   plugintools.log("###############"+finalurl)
   plugintools . play_resolved_url ( finalurl )     
    
run()