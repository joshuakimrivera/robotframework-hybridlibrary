# Robot Framework Hybrid Library main __init__.py file
# Copyright (C) 2019  Joshua Kim Rivera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import base64
from robotlibcore import keyword
from appium import webdriver

class SessionKeywords(object):
    
    @keyword
    def open_hybrid_application(self,    remoteUrl,
                                **kwargs
                                ):
        """Create a new session.
        """
        self.driver = webdriver.Remote( remoteUrl, kwargs)
        self.driver.implicitly_wait(self.implicitWait)

    @keyword
    def go_back(self):
        """Navigate backwards in the browser history, if possible (Web context only).
        """
        self.driver.back()
    
    @keyword
    def get_page_source(self):
        """Get the current application hierarchy XML (app) or page source (web).
        """
        return self.driver.page_source

    @keyword
    def take_screenshot(self, outputPath):
        """ Takes a screenshot of the viewport in a native context (iOS, Android) and takes a screenshot of the window in web context
            Note that some platforms may have settings that prevent screenshots from being taken, for security reason.
            One such feature is the Android FLAG_SECURE layout parameter.
        """
        imgdata = base64.b64decode(self.driver.get_screenshot_as_base64())
        filename = 'some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return 

    @keyword
    def close_application(self):
        """End the running session
        """
        self.driver.quit()

class ContextKeywords(object):
    
    @keyword
    def get_current_context(self):
        """ Get the current context in which Appium is running.
        """
        return self.driver.context

    @keyword
    def get_contexts(self):
        """ Get all the contexts available to automate.
        """
        return self.driver.contexts

    @keyword
    def set_context(self):
        """ Set the context being automated.
        """
