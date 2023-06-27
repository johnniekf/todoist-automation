<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi0.wp.com%2Fcyberpunklibrarian.com%2Fwp-content%2Fuploads%2F2018%2F09%2Ftodoist-logo.png%3Fssl%3D1&f=1&nofb=1&ipt=cf22f01fd125522fb88cbe729d7dd7452e9ba43ee78040a7ef082f9017197389&ipo=images" width="150" title="hover text">
</p>
<h1 align="center"><b>+</b></h1>
<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fclipart.info%2Fimages%2Fccovers%2F1590430652red-youtube-logo-png-xl.png&f=1&nofb=1&ipt=16b90db86daaee1f4d2a1351d0356f2cc438577e539abccb182a64402244c64e&ipo=images" width="200" title="hover text">
</p>

<h3>ToDoist Youtube tracker</h3>
<p>
  Simple python script using Google and Todoist API's to take a list of Youtube channel ID's from a Google Sheet and checked for videos uploaded in a 24hr timeframe then hyperlink any new videos as individual tasks on ToDoist labeled by the content creator.
<br><br>
  This project was made due to me occasionally wanting to closely follow certain content creator's series on a more direct basis due to Youtube's algorithm not always showing me new uploads by certain users.<br><br>
  This project can also be expanded to add filters for certain keywords in video titles (I.e. "Series X Ep:") to filter the content even more.
</p>

## Usage

To deploy this project you will need to install two dependencies

Google & ToDoist APIs:
```bash
  pip install google-api-python-client

  pip install todoist-api-python
```

Once these are installed you'll need to create a 'secret.json' file with the following contents:

```bash
  {
	"yt_api": "GOOGLE-API-KEY-HERE",
	"todoist_api": "TODOIST-API-KEY-HERE",
	"sheet_id": "GOOGLE-SHEET-ID-HERE"
}
```

## Obtaining API keys

ToDoist:

https://todoist.com/help/articles/find-your-api-token

Google:

* Create a project on: https://console.cloud.google.com/
* Assign your project API access to 'YouTube Data API v3' & 'Google Sheets API' then find your API key in the panel

Sheets ID:

* Configure a new sheet named anything you like
* Add Youtube channel id's vertically starting in cell 'A1' (Get Youtuber Channel IDs here: https://commentpicker.com/youtube-channel-id.php (this should be part of the project but as far as I can see searching channel IDs isn't possible in this version of the API))
* Find your sheet ID by looking at the url i.e. https://docs.google.com/spreadsheets/d/12345678910/ the string after '/d/' is your sheet ID. Prefereably you should set the securty options on the sheet to 'viewer' access by shared link just to be safe.

## Run the script!

```bash
  python3 todoist_automation.py
```

