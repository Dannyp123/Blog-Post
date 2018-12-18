from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

# Create your tests here.


class TestHomeView(TestCase):
    def test_render_home_template(self):
        response = self.client.get(reverse("home"))

        self.assertTemplateUsed(response, "home.html")


class TestNewPostView(TestCase):
    def test_render_new_post_template(self):
        response = self.client.get(reverse("new-post"))

        self.assertTemplateUsed(response, "new-post.html")

    @patch('app.forms.BlogPostForm')
    @patch('app.models.BlogPost.submit_post')
    def test_using_post_in_new_posts(self, submit_post, BlogPostForm):
        form = BlogPostForm.return_value
        form.is_valid.return_value = True
        response = self.client.post(reverse('new-post'))
        submit_post.assert_called_once()

    @patch('app.forms.BlogPostForm')
    @patch('app.models.BlogPost.submit_post')
    def test_using_post_in_new_posts_not(self, submit_post, BlogPostForm):
        form = BlogPostForm.return_value
        form.is_valid.return_value = False
        response = self.client.post(reverse('new-post'))
        submit_post.assert_not_called()



class TestBlogPostView(TestCase):
    @patch('app.models.BlogPost.objects.get')
    def test_render_blog_post_template(self, get):
        # the template blows up if we don't glue this together for
        # {% url ... blog.id %}
        # to work
        get.return_value.__getitem__.return_value = 1

        response = self.client.get(reverse("blog-post", kwargs={'id': 3}))
        get.assert_called_once_with(id=3)
        self.assertEqual(response.context['blog_post'], get.return_value)
        self.assertTemplateUsed(response, "blog-post.html")

    @patch('app.forms.BlogCommentForm')
    @patch('app.models.BlogComment.submit_comment')
    def test_using_post_in_new_comments(self, submit_comment, BlogCommentForm):
        form = BlogCommentForm.return_value
        form.is_valid.return_value = True
        response = self.client.post(reverse('make-comment', kwargs={'id': 3}))
        submit_comment.assert_called_once()

    @patch('app.forms.BlogCommentForm')
    @patch('app.models.BlogComment.submit_comment')
    def test_using_post_in_new_comments_not(self, submit_comment,
                                            BlogCommentForm):
        form = BlogCommentForm.return_value
        form.is_valid.return_value = False
        response = self.client.post(reverse('make-comment', kwargs={'id': 3}))
        submit_comment.assert_not_called()


class TestNewCommentView(TestCase):
    def test_render_new_comment_template(self):
        response = self.client.get(reverse('make-comment', kwargs={'id': 3}))

        self.assertTemplateUsed(response, 'comment.html')
