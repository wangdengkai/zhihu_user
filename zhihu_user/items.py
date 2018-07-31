# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class ZhihuUserItem(Item):
    s_followed = Field()
    avatar_url_template= Field()
    user_type= Field()
    answer_count= Field()
    is_following= Field()
    url= Field()
    type= Field()
    url_token= Field()
    id= Field()
    allow_message= Field()
    articles_count= Field()
    is_blocking= Field()
    name= Field()
    headline= Field()
    gender= Field()
    is_advertiser= Field()
    avatar_url= Field()
    is_org= Field()
    follower_count= Field()
    employments= Field()
    badge= Field()
    # # define the fields for your item here like:
    # # name = scrapy.Field()
    # id = Field()
    # name = Field()
    # account_status = Field()
    # allow_message= Field()
    # answer_count = Field()
    # articles_count = Field()
    # avatar_hue = Field()
    # avatar_url = Field()
    # avatar_url_template = Field()
    # badge = Field()
    # business = Field()
    # employments = Field()
    # columns_count = Field()
    # commercial_question_count = Field()
    # cover_url = Field()
    # description = Field()
    # educations = Field()
    # favorite_count = Field()
    # favorited_count = Field()
    # follower_count = Field()
    # following_columns_count = Field()
    # following_favlists_count = Field()
    # following_question_count = Field()
    # following_topic_count = Field()
    # gender = Field()
    # headline = Field()
    # hosted_live_count = Field()
    # is_active = Field()
    # is_bind_sina = Field()
    # is_blocked = Field()
    # is_advertiser = Field()
    # is_blocking = Field()
    # is_followed = Field()
    # is_following = Field()
    # is_force_renamed = Field()
    # is_privacy_protected = Field()
    # locations = Field()
    # is_org = Field()
    # type = Field()
    # url = Field()
    # url_token = Field()
    # user_type = Field()
    # logs_count = Field()
    # marked_answers_count = Field()
    # marked_answers_text = Field()
    # message_thread_token = Field()
    # mutual_followees_count = Field()
    # participated_live_count = Field()
    # pins_count = Field()
    # question_count = Field()
    # show_sina_weibo = Field()
    # thank_from_count = Field()
    # thank_to_count = Field()
    # thanked_count = Field()
    # type = Field()
    # vote_from_count = Field()
    # vote_to_count = Field()
    # voteup_count = Field()


# all_filed="""
#
#     {
#     "verb": "ANSWER_VOTE_UP",
#     "target": {
#         "relationship": {
#             "is_author": false,
#             "voting": 0,
#             "is_thanked": false,
#             "is_nothelp": false,
#             "upvoted_followee_ids": []
#         },
#         "mark_infos": [],
#         "excerpt": "从油管上看的，应该算不上巅峰，单纯觉得很萌。 Theo Jansen创造出了一系列依靠风力行走在海滩的机械怪物Strandbeests。 这个怪物的制作原理是利用直动机构。下面这个视频介绍了它的工作原理。",
#         "created_time": 1531388467,
#         "preview_type": "default",
#         "id": 440718383,
#         "is_copyable": true,
#         "author": {
#             "is_followed": false,
#             "type": "people",
#             "name": "熊哥哥CIEL",
#             "headline": "",
#             "url_token": "cielgao",
#             "user_type": "people",
#             "url": "https://api.zhihu.com/people/8c760fb1ada98c0c3417e11bbf8eae4a",
#             "avatar_url": "https://pic1.zhimg.com/50/9595c0fff_s.jpg",
#             "is_following": false,
#             "is_org": false,
#             "gender": 0,
#             "badge": [],
#             "id": "8c760fb1ada98c0c3417e11bbf8eae4a"
#         },
#         "url": "https://api.zhihu.com/answers/440718383",
#         "comment_permission": "all",
#         "question": {
#             "author": {
#                 "is_followed": false,
#                 "type": "people",
#                 "name": "铁佛爷",
#                 "headline": "业余徒步登山/业余港片爱好者/专业CS/坐标山东",
#                 "url_token": "tie-fo-ye",
#                 "user_type": "people",
#                 "url": "https://api.zhihu.com/people/13ffe59ddca27e068e133195e6cb82a7",
#                 "avatar_url": "https://pic1.zhimg.com/50/f05167c9fef9f4cd48710798f5b4543e_s.jpg",
#                 "is_following": false,
#                 "is_org": false,
#                 "gender": 1,
#                 "badge": [],
#                 "id": "13ffe59ddca27e068e133195e6cb82a7"
#             },
#             "created": 1522133814,
#             "url": "https://api.zhihu.com/questions/270090908",
#             "title": "纯机械时代的巅峰是什么？",
#             "excerpt": "本人是学cs的，忽然了解到机械差分机，感到很震撼。在今天没有人再会去设计这样的东西了。 故有此问，什么可称为纯机械时代的巅峰？差分机算吗？或者是枪械？手表？",
#             "answer_count": 214,
#             "bound_topic_ids": [
#                 285,
#                 464,
#                 4885,
#                 12014,
#                 16236
#             ],
#             "comment_count": 21,
#             "is_following": false,
#             "follower_count": 16221,
#             "type": "question",
#             "id": 270090908
#         },
#         "updated_time": 1531388859,
#         "content": "<p>从油管上看的，应该算不上巅峰，单纯觉得很萌。<br>Theo Jansen创造出了一系列依靠风力行走在海滩的机械怪物Strandbeests。</p><a class=\"video-box\" href=\"http://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1000795976529039360\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"true\" data-name=\"靠风力行走在海滩的机械怪物\" data-poster=\"https://pic4.zhimg.com/80/v2-44cb5c046435f6be73cd1730250f114b_b.jpg\" data-lens-id=\"1000795976529039360\">              <img class=\"thumbnail\" src=\"https://pic4.zhimg.com/80/v2-44cb5c046435f6be73cd1730250f114b_b.jpg\"><span class=\"content\">                <span class=\"title\">靠风力行走在海滩的机械怪物<span class=\"z-ico-extern-gray\"></span><span class=\"z-ico-extern-blue\"></span></span>                <span class=\"url\"><span class=\"z-ico-video\"></span>https://www.zhihu.com/video/1000795976529039360</span>              </span>            </a><p><br>这个怪物的制作原理是利用直动机构。下面这个视频介绍了它的工作原理。</p><a class=\"video-box\" href=\"http://link.zhihu.com/?target=https%3A//www.zhihu.com/video/1000796112122503168\" target=\"_blank\" data-video-id=\"\" data-video-playable=\"true\" data-name=\"Strandbeests机械原理\" data-poster=\"https://pic3.zhimg.com/v2-df5d21ef19f5d03a6584570aeb03f78e.jpg\" data-lens-id=\"1000796112122503168\">              <img class=\"thumbnail\" src=\"https://pic3.zhimg.com/v2-df5d21ef19f5d03a6584570aeb03f78e.jpg\"><span class=\"content\">                <span class=\"title\">Strandbeests机械原理<span class=\"z-ico-extern-gray\"></span><span class=\"z-ico-extern-blue\"></span></span>                <span class=\"url\"><span class=\"z-ico-video\"></span>https://www.zhihu.com/video/1000796112122503168</span>              </span>            </a>",
#         "comment_count": 436,
#         "voteup_count": 3628,
#         "reshipment_settings": "allowed",
#         "thanks_count": 415,
#         "excerpt_new": "从油管上看的，应该算不上巅峰，单纯觉得很萌。 Theo Jansen创造出了一系列依靠风力行走在海滩的机械怪物Strandbeests。 这个怪物的制作原理是利用直动机构。下面这个视频介绍了它的工作原理。",
#         "preview_text": "",
#         "can_comment": {
#             "status": true,
#             "reason": ""
#         },
#         "type": "answer",
#         "thumbnail": "https://pic4.zhimg.com/80/v2-44cb5c046435f6be73cd1730250f114b_b.jpg",
#         "thumbnail_extra_info": {
#             "show_maker_entrance": false,
#             "width": 1280,
#             "playlist": {
#                 "ld": {
#                     "url": "https://vdn.vzuu.com/Act-ss-m3u8-ld/83b6a60339e74e008d11f71c421984cb/707041de-85b7-11e8-b248-0242ac112a19.m3u8?auth_key=1532956614-0-0-22139f3a54a4ff185338c875ddc52aa4&expiration=1532956614&disable_local_cache=0",
#                     "width": 640,
#                     "size": 10087140,
#                     "height": 360
#                 },
#                 "hd": {
#                     "url": "https://vdn.vzuu.com/Act-ss-m3u8-hd/83b6a60339e74e008d11f71c421984cb/707041de-85b7-11e8-b248-0242ac112a19.m3u8?auth_key=1532956614-0-0-664e52bc67ee9a7872cfac792b910bb2&expiration=1532956614&disable_local_cache=0",
#                     "width": 1280,
#                     "size": 44692864,
#                     "height": 720
#                 },
#                 "sd": {
#                     "url": "https://vdn.vzuu.com/Act-ss-m3u8-sd/83b6a60339e74e008d11f71c421984cb/707041de-85b7-11e8-b248-0242ac112a19.m3u8?auth_key=1532956614-0-0-7284fc42cb6958c390550600b0838dfa&expiration=1532956614&disable_local_cache=0",
#                     "width": 848,
#                     "size": 18719160,
#                     "height": 478
#                 }
#             },
#             "url": "https://pic4.zhimg.com/80/v2-44cb5c046435f6be73cd1730250f114b_b.jpg",
#             "duration": 259,
#             "video_id": "1000795976529039360",
#             "type": "video",
#             "height": 720
#         }
#     },
#     "actor": {
#         "is_followed": false,
#         "type": "people",
#         "name": "郭启军",
#         "headline": "会点机械和嵌入式的后端萌新",
#         "url_token": "guo-qi-jun-58",
#         "user_type": "people",
#         "url": "https://api.zhihu.com/people/a2551205f5e76b2f9a6fe42c4aafe233",
#         "avatar_url": "https://pic4.zhimg.com/50/v2-52eeb6f1e4ecda4ddb94ced57975df43_s.jpg",
#         "is_following": false,
#         "is_org": false,
#         "gender": 1,
#         "badge": [],
#         "id": "a2551205f5e76b2f9a6fe42c4aafe233"
#     },
#     "action_text": "赞同了回答",
#     "created_time": 1531457773,
#     "type": "feed",
#     "id": "1531457773"
# }
# """