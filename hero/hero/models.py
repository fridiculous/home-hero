import json
import requests


class Property(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.photos = kwargs.get('photos')

    def analyze(self):
        with open('/data/phoenix.json') as data_file:
            data = json.load(data_file)

        return data


class User(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.city = kwargs.get('city')
        self.phone = kwargs.get('phone')
        self.profile_photo = kwargs.get('profile_photo')
        self.address = kwargs.get('address')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.property_type = kwargs.get('property_type')
        self.properties = kwargs.get('properties')

    def send_email(self):
        """Send user welcoming email about coming listing in the area. Using MailGun API
        """
        if self.email and self.name:

            title = '🚨 {name}, we have a job for you in {city} 🔨🏡'.format(
                name=self.name,
                city=self.city
            )

            # Listing
            listings_html = ""
            # Build out property list
            for listing in self.properties:
                listing_html = """
                    <tr name="listing" style="background:#f6f6f6">
                      <td class="padding-left" align="left" style="width:100px; padding:20px 20px 20px 40px; vertical-align:top;">
                          <img src="{image_url}" style="width:100px; height:100px; border-radius:4px; -moz-border-radius:4px; -webkit-border-radius:4px;">
                      </td>

                      <td class="padding-right" align="left" style="height:100px; padding:20px 40px 20px 0; vertical-align:top;">
                        <table cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                          <tr>
                            <td style="line-height:1.2em">
                                <span style="font-size:20px">${job_value}</span><br>
                                <span style="font-size:13px; color:#9e9e9e;">{distance_in_miles_from_user} mi. from you</span><br>
                                <span style="font-size:13px; color:#9e9e9e;">{beds}bd / {baths}ba<br>
                                </span>
                                <span style="font-size:13px">{listing_type}</span>
                            </td>
                          </tr>

                          <tr>
                            <td style="line-height:1.2em; font-size:12px; font-weight:600; color:#9e9e9e; padding-bottom:12px; padding-top:4px;">Updated Since {days_since_updated}</td>
                          </tr>

                          <tr>
                            <td align="left" style="padding:10px 0;">
                              <table cellspacing="0" cellpadding="0" border="0">
                                <tbody>
                                <tr><td align="center" width="140" height="42" bgcolor="#eb5635" style="-webkit-border-radius:4px; -moz-border-radius:4px; border-radius:4px; color: #ffffff;">
                                  <a href="{listing_url}" style="color: #ffffff; text-align:center; font-size:13px; font-weight:600; text-decoration:none; line-height:42px; height:42px; width:140px; display:block">View Job</a>
                                </td></tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                        </table>
                      </td>
                    </tr>
                """.format(
                    image_url=listing['media'][0]['url'].replace('https', 'http'),
                    job_value=round(listing['job_value'], 2),
                    beds=listing['bedrooms'],
                    baths=listing['baths'],
                    listing_type=listing['subtype'],
                    days_since_updated=listing['days_since_updated'],
                    listing_url=listing['mlsListingID'],
                    distance_in_miles_from_user=round(listing['distance_in_miles_from_user'], 1)
                )
                listings_html += listing_html

            message = """
                Congratulations {name}, You are truly awesome!
                We have a new job waiting for you at HomeHero.
                Log in at www.homehero.com to see your personalized listings <br/>
                <table>
                    {listings}
                </table>
            """.format(
                name=self.name,
                listings=listings_html
            )

            receiver = "{0} <{1}>".format(self.name, self.email)

            result = requests.post(
                "https://api.mailgun.net/v3/sandbox26be8ec8c16b4ffcb59bed7de331e02a.mailgun.org/messages",
                auth=("api", "key-77d3a52368726ba807ce46aa3a70f5e4"),
                data={"from": "HomeHero <hello@homehero.com>",
                      "to": [receiver],
                      "subject": title,
                      "html": message})
            if result.status_code == 200:
                return {'status': 'sent successful to {0} at {1}'.format(self.name, self.email)}
        return {'status': 'failed'}
