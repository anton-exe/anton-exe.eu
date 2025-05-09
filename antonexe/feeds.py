from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from main.models import BlogPost


class BlogHTMLFeedGenerator(Rss201rev2Feed):
    def rss_attributes(self):
        attrs = super().rss_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        return attrs

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        if 'content_encoded' in item:
            handler._write('<content:encoded><![CDATA[%s]]></content:encoded>' % item['content_encoded'])


class BlogRSS(Feed):
    feed_type = BlogHTMLFeedGenerator
    title = "anton-exe.eu blog"
    link = "/"
    description = "my personal blog that i may or may not use"
    language = "en"

    def items(self):
        return BlogPost.objects.order_by("-creation_date")[:100]

    def item_title(self, item):
        return item.title

    def item_author_name(self, item):
        return item.author

    def item_description(self, item):
        return item.content  # still used as a fallback, but escaped

    def item_extra_kwargs(self, item):
        return {'content_encoded': item.content}

    def item_pubdate(self, item):
        return item.creation_date
