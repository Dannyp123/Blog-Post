from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    cover_img_url = models.URLField()

    def __str__(self):
        return '''
        User Image: {}
        Title: {}
        Body: {}
        Author: {}
        Date: {}
        
        '''.format(self.cover_img_url, self.title, self.body, self.author,
                   self.date)

    @staticmethod
    def submit_post(title, body, author):
        BlogPost(title=title, body=body, author=author).save()


class BlogComment(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.PROTECT)

    def __str__(self):
        return '''
        Title: {}
        Author: {}
        Body: {}
        Rating: {}
        Date: {}
        Comment for Blog #: {}
        '''.format(self.title, self.author, self.body, self.rating, self.date,
                   self.blog_post)

    @staticmethod
    def submit_comment(title, body, author, rating, blog_post_id):
        BlogComment(
            title=title,
            body=body,
            author=author,
            rating=rating,
            blog_post_id=blog_post_id).save()
