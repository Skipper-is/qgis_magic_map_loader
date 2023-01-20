# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MAGICMapLoader
                                 A QGIS plugin
 This plugin will open the DEFRA MAGIC Map service on the area of your map canvas
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-20
        copyright            : (C) 2023 by DeltaV Geospatial
        email                : David@DeltaVGeo.co.uk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MAGICMapLoader class from file MAGICMapLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .magic_map_loader import MAGICMapLoader
    return MAGICMapLoader(iface)
