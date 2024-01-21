.. include:: /global/godot_api.rst

.. _api_RetroAchievements_Raw:

RetroAchievements.Raw
=====================

This class exposes the RetroAchievements' raw API for any advanced use cases.

.. note::

	This API wraps the `RetroAchievements' official API endpoints <https://api-docs.retroachievements.org/>`__. You should refer to it for details on each API call and arguments.

.. note::

	Almost all requests require you to supply an authentication |godot_dictionary|, which can be obtained through :ref:`RetroAchievements.build_auth <api_RetroAchievements_build_auth>`.

Methods
-------

.. list-table::
	:widths: 20 80
	:header-rows: 1

	* - Type
	  - Name
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_achievement_of_the_week <api_RetroAchievements_Raw_get_achievement_of_the_week>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_claims <api_RetroAchievements_Raw_get_claims>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_active_claims <api_RetroAchievements_Raw_get_active_claims>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_top_ten_users <api_RetroAchievements_Raw_get_top_ten_users>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_recent_achievements <api_RetroAchievements_Raw_get_user_recent_achievements>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_achievements_earned_between <api_RetroAchievements_Raw_get_achievements_earned_between>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_achievements_earned_on_day <api_RetroAchievements_Raw_get_achievements_earned_on_day>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_game_info_and_user_progress <api_RetroAchievements_Raw_get_game_info_and_user_progress>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_awards <api_RetroAchievements_Raw_get_user_awards>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_claims <api_RetroAchievements_Raw_get_user_claims>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_completed_games <api_RetroAchievements_Raw_get_user_completed_games>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_game_rank_and_score <api_RetroAchievements_Raw_get_user_game_rank_and_score>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_points <api_RetroAchievements_Raw_get_user_points>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_progress <api_RetroAchievements_Raw_get_user_progress>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_recently_played_games <api_RetroAchievements_Raw_get_user_recently_played_games>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_user_summary <api_RetroAchievements_Raw_get_user_summary>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_achievement_count <api_RetroAchievements_Raw_get_achievement_count>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_achievement_distribution <api_RetroAchievements_Raw_get_achievement_distribution>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_game <api_RetroAchievements_Raw_get_game>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_game_extended <api_RetroAchievements_Raw_get_game_extended>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_game_rank_and_score <api_RetroAchievements_Raw_get_game_rank_and_score>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_console_ids <api_RetroAchievements_Raw_get_console_ids>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_game_list <api_RetroAchievements_Raw_get_game_list>`
	* - :ref:`Raw.Response <api_RetroAchievements_Raw_Response>`
	  - :ref:`get_achievement_unlocks <api_RetroAchievements_Raw_get_achievement_unlocks>`

----

.. _api_RetroAchievements_Raw_get_achievement_of_the_week:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_achievement_of_the_week** (|godot_dictionary| auth)

`API_GetAchievementOfTheWeek.php <https://api-docs.retroachievements.org/v1/events/achievement-of-the-week.html>`_

----

.. _api_RetroAchievements_Raw_get_claims:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_claims** (|godot_dictionary| auth, |godot_string| kind)

`API_GetClaims.php <https://api-docs.retroachievements.org/v1/feed/get-claims.html>`_

----

.. _api_RetroAchievements_Raw_get_active_claims:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_active_claims** (|godot_dictionary| auth)

`API_GetActiveClaims.php <https://api-docs.retroachievements.org/v1/feed/get-active-claims.html>`_

----

.. _api_RetroAchievements_Raw_get_top_ten_users:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_top_ten_users** (|godot_dictionary| auth)

`API_GetTopTenUsers.php <https://api-docs.retroachievements.org/v1/feed/get-top-ten-users.html>`_

----

.. _api_RetroAchievements_Raw_get_user_recent_achievements:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_recent_achievements** (|godot_dictionary| auth, |godot_string| username, |godot_int| recent_minutes = ``60``)

`API_GetUserRecentAchievements.php <https://api-docs.retroachievements.org/v1/users/recent-achievements.html>`_

----

.. _api_RetroAchievements_Raw_get_achievements_earned_between:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_achievements_earned_between** (|godot_dictionary| auth, |godot_string| username, |godot_int| from_date, |godot_int| to_date)

`API_GetAchievementsEarnedBetween.php <https://api-docs.retroachievements.org/v1/users/achievements-earned-between.html>`_

----

.. _api_RetroAchievements_Raw_get_achievements_earned_on_day:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_achievements_earned_on_day** (|godot_dictionary| auth, |godot_string| username, |godot_string| on_date)

`API_GetAchievementsEarnedOnDay.php <https://api-docs.retroachievements.org/v1/users/achievements-earned-on-day.html>`_

----

.. _api_RetroAchievements_Raw_get_game_info_and_user_progress:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_game_info_and_user_progress** (|godot_dictionary| auth, |godot_string| username, |godot_int| game_id)

`API_GetGameInfoAndUserProgress.php <https://api-docs.retroachievements.org/v1/users/game-progress.html>`_

----

.. _api_RetroAchievements_Raw_get_user_awards:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_awards** (|godot_dictionary| auth, |godot_string| username)

`API_GetUserAwards.php <https://api-docs.retroachievements.org/v1/users/user-awards.html>`_

----

.. _api_RetroAchievements_Raw_get_user_claims:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_claims** (|godot_dictionary| auth, |godot_string| username)

`API_GetUserClaims.php <https://api-docs.retroachievements.org/v1/users/get-user-claims.html>`_

----

.. _api_RetroAchievements_Raw_get_user_completed_games:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_completed_games** (|godot_dictionary| auth, |godot_string| username)

`API_GetUserCompletedGames.php <https://api-docs.retroachievements.org/v1/users/completed-games.html>`_

----

.. _api_RetroAchievements_Raw_get_user_game_rank_and_score:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_game_rank_and_score** (|godot_dictionary| auth, |godot_string| username, |godot_int| game_id)

`API_GetUserGameRankAndScore.php <https://api-docs.retroachievements.org/v1/users/get-user-game-rank-and-score.html>`_

----

.. _api_RetroAchievements_Raw_get_user_points:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_points** (|godot_dictionary| auth, |godot_string| username)

`API_GetUserPoints.php <https://api-docs.retroachievements.org/v1/users/get-user-points.html>`_

----

.. _api_RetroAchievements_Raw_get_user_progress:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_progress** (|godot_dictionary| auth, |godot_string| username, |godot_array| [ |godot_int| ] game_ids)

`API_GetUserProgress.php <https://api-docs.retroachievements.org/v1/users/get-user-progress.html>`_

----

.. _api_RetroAchievements_Raw_get_user_recently_played_games:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_recently_played_games** (|godot_dictionary| auth, |godot_string| username, |godot_int| count = ``10``, |godot_int| offset = ``0``)

`API_GetUserRecentlyPlayedGames.php <https://api-docs.retroachievements.org/v1/users/get-user-recently-played-games.html>`_

----

.. _api_RetroAchievements_Raw_get_user_summary:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_user_summary** (|godot_dictionary| auth, |godot_string| username, |godot_int| recent_games_count = ``0``, |godot_int| recent_achievements_count = ``5``)

`API_GetUserSummary.php <https://api-docs.retroachievements.org/v1/users/get-user-summary.html>`_

----

.. _api_RetroAchievements_Raw_get_achievement_count:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_achievement_count** (|godot_dictionary| auth, |godot_int| game_id)

`API_GetAchievementCount.php <https://api-docs.retroachievements.org/v1/games/achievement-ids.html>`_

----

.. _api_RetroAchievements_Raw_get_achievement_distribution:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_achievement_distribution** (|godot_dictionary| auth, |godot_int| game_id)

`API_GetAchievementDistribution.php <https://api-docs.retroachievements.org/v1/games/achievement-distribution.html>`_

----

.. _api_RetroAchievements_Raw_get_game:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_game** (|godot_dictionary| auth, |godot_int| game_id)

`API_GetGame.php <https://api-docs.retroachievements.org/v1/games/summary.html>`_

----

.. _api_RetroAchievements_Raw_get_game_extended:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_game_extended** (|godot_dictionary| auth, |godot_int| game_id)

`API_GetGameExtended.php <https://api-docs.retroachievements.org/v1/games/detailed-info.html>`_

----

.. _api_RetroAchievements_Raw_get_game_rank_and_score:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_game_rank_and_score** (|godot_dictionary| auth, |godot_int| game_id, |godot_string| type)

`API_GetGameRankAndScore.php <https://api-docs.retroachievements.org/v1/games/high-scores.html>`_

----

.. _api_RetroAchievements_Raw_get_console_ids:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_console_ids** (|godot_dictionary| auth)

`API_GetConsoleIDs.php <https://api-docs.retroachievements.org/v1/consoles/all-systems.html>`_

----

.. _api_RetroAchievements_Raw_get_game_list:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_game_list** (|godot_dictionary| auth, |godot_int| console_id, |godot_bool| should_only_retrieve_games_with_achievements = ``false``, |godot_bool| should_retrieve_game_hashes = ``false``)

`API_GetGameList.php <https://api-docs.retroachievements.org/v1/consoles/all-games.html>`_

----

.. _api_RetroAchievements_Raw_get_achievement_unlocks:

	:ref:`Raw.Response <api_RetroAchievements_Raw_Response>` **get_achievement_unlocks** (|godot_dictionary| auth, |godot_int| achievement_id, |godot_int| count = ``50``, |godot_int| offset = ``0``)

`API_GetAchievementUnlocks.php <https://api-docs.retroachievements.org/v1/achievements/get-achievement-unlocks.html>`_