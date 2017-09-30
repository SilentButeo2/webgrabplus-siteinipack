<?php

/*rename this php file to dsmart.php*/

        $ch = curl_init();
        $agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/51.0';
        $reqtype = $_GET['reqtype'];

             if($reqtype == '1') {
               $channel = $_GET['channel'];
       	       $date = $_GET['date'];
	             $url = "https://www.dsmart.com.tr/actions/schedule?channel_id=" . $channel . "&day=" . $date;
               curl_setopt($ch, CURLOPT_HTTPHEADER, array('Accept: application/json'));
             } elseif($reqtype == '2') {
                   $programid = $_GET['programid'];
                   $url = "https://www1.dsmart.com.tr/Page/Popup/TvGuide/ProgramDetail2.aspx?cacheID=" . $programid . "&bouquetID=&TrafficKey=" . $programid;
                   curl_setopt($ch, CURLOPT_HTTPHEADER, array('X-Requested-With: XMLHttpRequest', 'Content-Length: ' . strlen($postdata)));
        }

	      curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_USERAGENT, $agent);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

        $output = curl_exec($ch);

        curl_close($ch);

        echo $output;
?>
