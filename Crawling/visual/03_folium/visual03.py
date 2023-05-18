import folium
import json

# 1. starbucks01.json 파일을 읽어드리자
with open('starbucks01.json', 'r', encoding='utf-8') as f:
    sb_data = json.load(f)

# 2. 지도 만들자
sb_map = folium.Map(location=[37.503550462750475, 127.0497652689724], zoom_start=18)

# 3. starbucks01.json 파일을 읽어드린 내용 (1에서 실행한 결과)을 가지고
#    반복해서 starbucks 매장의 marker를 만들어 지도에 추가하자
for sb in sb_data['store_list']:
    folium.Marker([sb['lat'], sb['lot']],
                  popup=folium.Popup(sb['s_name'], max_width=100)).add_to(sb_map)

# 4. 지도 저장하자
sb_map.save('visual03.html')