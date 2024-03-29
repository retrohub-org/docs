.. include:: /global/rh_actions.rst
.. _userguide_scraping:

Scraping
========

A scraper is a tool that can automatically fetch a game's metadata and download associated media. RetroHub supports the following scrapers:

- `ScreenScraper <https://www.screenscraper.fr/>`_

Usage
-----

.. note::
	It's recommended to use keyboard and mouse during the scraping process, as you might need plenty of text input and navigating through lists.

You can scrape one, multiple, or even your entire library of games. Open the **Settings** (|action: rh_menu|) menu and select the **Scraper** tab.

.. image:: assets/scraper_settings.png

Select the desired scraping service. Different scrapers will have different levels of `Search Support`_, `Metadata Support`_ and `Media Support`_.

.. note::
	We recommend using ScreenScraper as it is the most complete scraper right now.

.. image:: assets/scraper_settings_search.png

Check how to search for your games:

- **By file hash**: Computes the MD5 hash of your game files and uses it to uniquely identify it on the scraper's database. This is the most reliable way to detect your games. If this doesn't work (either because the file is too big, or the scraper doesn't know that hash), it will fallback to search by name if enabled.
- **By file name**: Searches for your game using the game's file name, minus the extension. RetroHub will ask you to choose between multiple results if available, and also allow you to refine the search term.
- **File hash size limit**: When searching by hash is enabled, this option allows you to set the maximum file size (in MB/GB) allowed. Files bigger than this will not be hashed, and will fallback to search by name if enabled.

.. image:: assets/scraper_settings_media.png

Check what kind of information you want to scrape:

- **Metadata**: Game textual information (name, description, release date, etc.)
- **Media**: Game media (box art, screenshots, videos, etc.)

Then check each type of media you wish to scrape.

.. image:: assets/scraper_settings_game.png

Lastly, select what games you want to scrape, and start the process by clicking the **Scrape now!** button.

Depending on the amount of games, types of media, and your internet connection, this process may take quite some time to complete. A new popup will appear where you can accompany the progress for each game, as well as fix problems found for some games (such as game title not found, multiple results available, etc...)

.. image:: assets/scraper_process.png

.. warning::
	For large game libraries, the media files can start to take up a lot of space (>1GB). Ensure you have enough free space on your hard drive before scraping, as this may fill your entire disk space.

ScreenScraper
-------------

Region
^^^^^^
ScreenScraper will return results according to your currently set region, and not the game's region.

API quota
^^^^^^^^^
ScreenScraper has both a daily and hourly quota for API requests. If this limit is reached, RetroHub will start showing errors when scraping.

To circumvent this, you should make a free account on their website at `https://www.screenscraper.fr/ <https://www.screenscraper.fr/>`_ and enter your credentials in the **Scraper** settings:

.. image:: assets/scraper_ss_account.png

This will scrape with your personal quota instead. If that runs out as well, you'll have to wait until the next day/hour to scrape again.

Thread usage
^^^^^^^^^^^^

By default, RetroHub will scrape with 2 threads. If your custom account has access to more threads, RetroHub will use all of them. To limit how many threads are used, you can set it in the **Scraper** settings:

.. image:: assets/scraper_ss_threads.png

Search Support
--------------

+-------------------+---------------+
| Search            | ScreenScraper |
+===================+===============+
| File hash         | yes           |
+-------------------+---------------+
| File name         | yes           |
+-------------------+---------------+

Metadata Support
----------------

+-------------------+---------------+
| Metadata          | ScreenScraper |
+===================+===============+
| Name              | yes           |
+-------------------+---------------+
| Description       | yes           |
+-------------------+---------------+
| Rating            | yes           |
+-------------------+---------------+
| Release Date      | yes           |
+-------------------+---------------+
| Developer         | yes           |
+-------------------+---------------+
| Publisher         | yes           |
+-------------------+---------------+
| Genres            | yes           |
+-------------------+---------------+
| Number of players | yes           |
+-------------------+---------------+
| Age Rating        | yes           |
+-------------------+---------------+

Media Support
-------------

+-------------------+---------------+
| Media             | ScreenScraper |
+===================+===============+
| Logo              | yes           |
+-------------------+---------------+
| Screenshot        | yes           |
+-------------------+---------------+
| Title Screen      | yes           |
+-------------------+---------------+
| Video             | yes           |
+-------------------+---------------+
| Box Render        | yes           |
+-------------------+---------------+
| Box Texture       | yes           |
+-------------------+---------------+
| Support Render    | yes           |
+-------------------+---------------+
| Support Texture   | yes           |
+-------------------+---------------+
| Manual            | yes           |
+-------------------+---------------+


