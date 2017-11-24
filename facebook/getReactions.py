import facebook
import requests

token = 'EAAB3mrMknIoBAPBZBG8sviLdmrfrrDup5KXxLY9st1FkiiIT6NXkBot9pJbu4T5GfyBAtmu3DE3gFeAr7u71IL6QWkZCZCHXTQYRn9MkP6dXHRvZCyksdBBjvoq3JOosZBoZCWxIsvlsIrbMWvMLAvOUNhbhrOD4UZD'

graph = facebook.GraphAPI(access_token=token, version = 2.7)
events = graph.request('/search?q=Poetry&type=event&limit=10000')

pagesdata = requests.get("https://graph.facebook.com/me/accounts?access_token="+token)
page_id = "161674417186975"
posts_on_page = requests.get("https://graph.facebook.com/"+page_id+"/feed?access_token="+token)
posts_data = (posts_on_page.json())
#print posts_data
for x in posts_data['data']:
 post_id = x['id']
 reactions_on_post = requests.get("https://graph.facebook.com/"+post_id+"/reactions?access_token="+token)
 reactions_data = reactions_on_post.json()
 print reactions_data
