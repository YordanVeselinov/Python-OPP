from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.media = SocialMedia(
            "BTV",
            "YouTube",
            100_000,
            "Posts"
        )

    def test_init_expect_success(self):
        self.assertEqual("BTV", self.media._username)
        self.assertEqual("YouTube", self.media._platform)
        self.assertEqual(100_000, self.media.followers)
        self.assertEqual("Posts", self.media._content_type)
        self.assertEqual([], self.media._posts)

    def test_followers_setter_expect_value_error(self):
        expected_output = "Followers cannot be negative."

        with self.assertRaises(ValueError) as ex:
            self.media.followers = -1000

        self.assertEqual(str(ex.exception), expected_output)

    def test_platform_setter_expect_value_error(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        expected_output = f"Platform should be one of {allowed_platforms}"

        with self.assertRaises(ValueError) as ex:
            self.media.platform = "ERROR"

        self.assertEqual(expected_output, str(ex.exception))

    def test_create_post_expected_success(self):
        expected_output = f"New {self.media._content_type} post created by {self.media._username} on {self.media._platform}."
        result = self.media.create_post("Some contend")

        self.assertEqual(expected_output, result)
        self.assertEqual(self.media._posts, [{'content': 'Some contend', 'likes': 0, 'comments': []}])

    def test_like_post_expect_index_out_of_range(self):
        expected_output = "Invalid post index."
        result = self.media.like_post(200)

        self.assertEqual(expected_output, result)

    def test_like_post_expected_success(self):
        expected = f"Post liked by {self.media._username}."

        self.media.create_post("Random")
        result = self.media.like_post(0)

        likes = self.media._posts[0]["likes"]
        self.assertEqual(expected, result)
        self.assertEqual(1, likes)

    def test_like_post_with_more_than_10_likes(self):
        expected = "Post has reached the maximum number of likes."

        self.media.create_post("Random")
        self.media._posts[0]["likes"] = 200

        result = self.media.like_post(0)

        self.assertEqual(expected, result)

    def test_comment_on_post_with_less_then_10_characters(self):
        expected = "Comment should be more than 10 characters."

        self.media.create_post("Random")

        result = self.media.comment_on_post(0, "small")

        self.assertEqual(expected, result)

    def test_comment_on_post_with_more_than_10_characters(self):
        expected = f"Comment added by {self.media._username} on the post."

        self.media.create_post("Random")

        result = self.media.comment_on_post(0, "More than 10 characters so its good!")

        self.assertEqual(expected, result)

        result_comment = self.media._posts[0]["comments"]

        expected_comment = [{'comment': 'More than 10 characters so its good!', 'user': 'BTV'}]

        self.assertEqual(result_comment, expected_comment)



if __name__ == "__main__":
    main()
