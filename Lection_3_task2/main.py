import html_creater as hc
import xml_gerenator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

hc.new_create(xg.new_create(dp.data_collection())) # получаем данные, пробрасываем в метод, который отвечает за xml-генерацию