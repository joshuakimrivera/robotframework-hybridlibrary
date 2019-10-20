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

from robotlibcore import keyword

class ElementFinder(object):

    def __init__(self):
        """
        """

    @keyword
    def find_element(self,locator):
        return self._element_finder(locator)

    def _element_finder(self,locator):
        return self.driver.find_element_by_id(locator)