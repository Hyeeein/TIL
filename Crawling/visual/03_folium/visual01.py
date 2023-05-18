import folium

# 구글 지도에서 마커 복사하면 아래 주소 알아서 복사됨
my_loc = folium.Map(location=[37.503550462750475, 127.0497652689724], zoom_start=18)
my_loc.save('visual01.html')