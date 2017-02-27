**------------------------------------------------------------------------------------------------
* @header_start
* WebGrab+Plus ini for grabbing EPG data from TvGuide websites
* @Site: your_site_name
* @MinSWversion:
* @Revision 0 - [26/02/2017] Netuddki
*     - create
* @Remarks: your_remarks
* @header_end
**------------------------------------------------------------------------------------------------

site {url=telecom.ch|timezone=Europe/Zurich|maxdays=7|cultureinfo=de-CH|charset=UTF-8|titlematchfactor=90}
site {ratingsystem=DE|episodesystem=onscreen|}
url_index{url|http://www.teleclub.ch/guide/tv/|urldate|}
urldate.format {datestring|yyyy/MM/dd}

scope.range{(urlindex)|end}
index_variable_element.modify {set|'config_site_id'}
index_variable_element.modify {replace|'config_site_id'|key="'config_site_id'">}
end_scope
*
index_showsplit.scrub {multi(includeblock="'index_variable_element'")|<li class="channel|<li class="time-pos||</ul>}
index_urlshow {url|http://www.teleclub.ch|<a href|="|"|rel="}
*index_urlchannellogo {url| }
*
index_start.scrub {single|data-time=|"|"|data-duration}
index_stop.scrub {regex||<span class="time end-time">(\d{2}).*(\d{2})||}
*
index_title.scrub {single|<span class="name">||</span>|</span>} 
*
title.scrub {single|<div class="lightbox-header">|<h2>|</h2>|</div>}
category.scrub {single|<div class="lightbox-header">|<h3>|</h3>|</div>}
subtitle.scrub {multi(separator="<p>" include=first)|<div class="lightbox-content|<p>|</p>|<div class="lightbox-footer">}
description.scrub {multi(separator="<p>" exclude=first)|<div class="lightbox-content|<p>|</p>|<div class="lightbox-footer">}
*
*
productiondate.scrub {regex||(<dt>Produktion</dt>.*(\d{4})</span>)||}
showicon.scrub {url|http://www.teleclub.ch|<div class="lightbox-media">|src="|"|</div>} 
director.scrub {single(separator="<br />")|<strong>Regie|</strong>|</p>|<div class="lightbox-footer">}
actor.scrub {single(separator="<br />"", ")|<strong>Darsteller|</strong>|</p>|<div class="lightbox-footer">}
*
rating.scrub {regex||title="Altersfreigabe (E\d+)||}
rating.modify{replace|E|FSK}
temp_1.modify {substring(type=regex)|'description' "Ab\s(\d+)\sJahren"}
rating.modify {addstart('temp_1' not "")|FSK'temp_1'}

temp_2.modify {substring(type=regex)|'description' "[A-Z]+\s(\d{4}),"}
productiondate.modify {addstart('temp_2' not "")|'temp_2'}
*
temp_4.modify {substring(type=regex)|'description' "([A-Z]+)\s\d{4},"}
country.modify {addstart('temp_4' not "")|'temp_4'}
*
temp_5.modify {substring(type=regex)|'description' "([A-Z]+)\s\d{4}\."}
country.modify {addstart('temp_5' not "")|'temp_5'}
*
temp_6.modify {substring(type=regex)|'description' "(\d{4})\."}
productiondate.modify {addstart('temp_6' not "")|'temp_6'}
*
actor.modify {substring(type=regex)|'description' "(?:\d{4}, mit *(.*?))\."}
description.modify {remove(type=regex)|(\d{4}, mit *(.*?)\.)}
*
description.modify {remove(type=regex)|(Ab\s\d+\sJahren)}
description.modify {remove(type=regex)|(\d+\sMin\.)}
description.modify {remove(type=regex)|([A-Z]+\s)}
description.modify {remove(type=regex)|(\d{4}\.)}
description.modify {remove(type=regex)|(\d{4},)}
country.scrub {single|<span class="mini-desc-icon"|<i>|</i>|</span>}
ratingicon.scrub {url|http://www.teleclub.ch|<dt>Freigabe</dt>
|background-image: url(|)">|</span>}
*
*
**  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _
**      #####  CHANNEL FILE CREATION (only to create the xxx-channel.xml file)
**
** @auto_xml_channel_start
*url_index{url|http://www.teleclub.ch/guide/tv}
*index_site_channel.scrub {multi|<li class="channel|<img alt="|"|src}
*index_site_id.scrub {multi|<li class="channel|data-key="|"|>}
** @auto_xml_channel_end
