**------------------------------------------------------------------------------------------------
* @header_start
* WebGrab+Plus ini for grabbing EPG data from TvGuide websites
* @Site: alaoula.ma
* @MinSWversion: 3.1
* @Revision 0 - [20/05/2022] Mat8861
*     
* @Remarks:
* @header_end
**------------------------------------------------------------------------------------------------

site {url=alaoula.ma|timezone=Africa/Casablanca|maxdays=4|cultureinfo=ar-AR|charset=UTF-8|titlematchfactor=90}
*
url_index{url|http://www.alaoula.ma/programmes.php?jr=|urldate|&lang=ar}
url_index.headers {customheader=Accept-Encoding=gzip,deflate}
url_index.headers {accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9}
urldate.format {datestring|dd/MM/yyyy|en-GB}
*
index_showsplit.scrub {multi|<table width="820" cellpadding="0" cellspacing="0" border="0" align="center">|<td height="30" width="100" align="center" class="grille_time_cell_off" >||</table>}
index_showsplit.modify {cleanup(removeduplicates span=2 keeplast)}
index_start.scrub {single|<div class="grille_time_off|>|</div>|</div>}
index_title.scrub {single|<div class="grille_item_title_holder">||</div>|</div>}
index_title.modify {cleanup(tags="<"">")} 
index_urlchannellogo.modify {addstart|http://www.alaoula.ma/images/alaoula.png}

**  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _
**      #####  CHANNEL FILE CREATION (only to create the xxx-channel.xml file)
**
** @auto_xml_channel_start
*index_site_id.scrub {|}
*index_site_id.modify {set|alaoula}
*index_site_channel.modify {set|Alaoula TV}
** @auto_xml_channel_end
