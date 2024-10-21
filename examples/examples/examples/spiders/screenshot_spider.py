import scrapy
from scrapy_zenrows import ZenRowsRequest
import base64
import json


class ScreenshotSpider(scrapy.Spider):
    name = "screenshot_spider"

    def start_requests(self):
        url = "https://www.scrapingcourse.com/ecommerce/"
        # request screenshot with specific parameters
        yield ZenRowsRequest(
            url=url,
            callback=self.parse,
            params={
                "js_render": "true",
                "json_response": "true",
                "screenshot": "true",
                "screenshot_fullpage": "true",
                "screenshot_format": "jpeg",
                "screenshot_quality": "80",
                "wait": "5000",  # wait for 5 seconds for page to load
            },
        )

    def parse(self, response):
        try:
            # parse JSON response
            data = json.loads(response.text)
            screenshot_data = data.get("screenshot", {})

            if screenshot_data:
                # decode and save screenshot
                image_data = base64.b64decode(screenshot_data["data"])
                image_type = screenshot_data["type"].split("/")[-1]
                filename = f"ecommerce_fullpage_screenshot.{image_type}"

                with open(filename, "wb") as f:
                    f.write(image_data)

                self.logger.info(f"Screenshot saved as {filename}")
                self.logger.info(
                    f"Image dimensions: {screenshot_data['width']}x{screenshot_data['height']} pixels"
                )

                # yield screenshot information
                yield {
                    "screenshot_filename": filename,
                    "screenshot_dimensions": f"{screenshot_data['width']}x{screenshot_data['height']}",
                    "screenshot_type": screenshot_data["type"],
                }
            else:
                self.logger.error("No screenshot data found in the response")

        except json.JSONDecodeError:
            self.logger.error("Failed to parse JSON response")
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
