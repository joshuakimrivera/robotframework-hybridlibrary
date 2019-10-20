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

from appium import webdriver
from ..utils import ElementFinder

class MouseKeywords(ElementFinder):

    def click_element(self, locator):
        """Click any mouse button at the current mouse coordinates
        """
        actions = ActionChains(self.driver)
        element = ElementFinder.find_element(locator)
        actions.move_to_element(element)
        actions.click()
        actions.perform()