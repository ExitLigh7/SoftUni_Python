from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.media = SocialMedia(
            "Testy", "YouTube", 200, "fun"
        )

        self.media_with_posts = SocialMedia(
            "More", "Twitter", 100, "vlog"
        )
        self.media_with_posts._posts = [{'content': "Adds", 'likes': 0, 'comments': []}]

    def test_correct_init(self):
        self.assertEqual("Testy", self.media._username)
        self.assertEqual("YouTube", self.media.platform)
        self.assertEqual(200, self.media.followers)
        self.assertEqual("fun", self.media._content_type)
        self.assertEqual([], self.media._posts)

    def test_init_with_negative_followers_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.media.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_validate_and_set_platform_with_not_allowed_platform(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ve:
            self.media.platform = "Not Allowed"

        self.assertEqual(
            f"Platform should be one of {allowed_platforms}",
            str(ve.exception)
        )

    def test_create_post_appends_to_posts_list(self):
        post_content = "Test post"
        self.assertEqual(f"New {self.media._content_type} post created by"
                         f" {self.media._username} on {self.media._platform}.",
                         self.media.create_post(post_content)
                         )

        self.assertEqual(
            [{'content': post_content, 'likes': 0, 'comments': []}],
            self.media._posts
        )

    def test_like_post_successfully(self):
        self.assertEqual(f"Post liked by {self.media_with_posts._username}.",
                         self.media_with_posts.like_post(0)
                         )

        self.assertEqual([{'content': "Adds", 'likes': 1, 'comments': []}],
                         self.media_with_posts._posts
                         )

    def test_like_post_with_reached_max_likes_return_error_msg(self):
        self.media_with_posts._posts[0]["likes"] = 10

        self.assertEqual("Post has reached the maximum number of likes.",
                         self.media_with_posts.like_post(0)
                         )

    def test_like_post_with_invalid_post_index(self):
        self.assertEqual("Invalid post index.",
                         self.media.like_post(0)
                         )

    def test_comment_on_post_successfully(self):
        comment = "Test comment"

        self.assertEqual(f"Comment added by {self.media_with_posts._username} on the post.",
                         self.media_with_posts.comment_on_post(0, comment)
                         )

        self.assertEqual(
            [{'content': "Adds", 'likes': 0, 'comments':
                [{'user': self.media_with_posts._username, 'comment': comment}]}],
            self.media_with_posts._posts

        )

    def test_comment_on_post_with_comment_less_than_ten_chars(self):
        comment = "Not ten"

        self.assertEqual(
            "Comment should be more than 10 characters.",
            self.media_with_posts.comment_on_post(0, comment)
        )


if __name__ == "__main__":
    main()
