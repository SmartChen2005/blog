---
layout: page
title: "Search"
description: "Smart Chen的私人搜索平台"
header-img: "img/twitter.jpg"
---

<script language="javascript">
function baidu()
{
	if(document.search.text.value=="")
	{
		alert("你貌似什么都没有输入···");
	}else{
		var baidu_search = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd="+document.search.text.value;
	window.open(baidu_search);
	}
}
function google()
{
	if(document.search.text.value=="")
	{
		alert("你貌似什么都没有输入···");
	}else{
		var google_search = "https://www.google.com/search?q="+document.search.text.value+"&ie=utf-8&oe=utf-8"
	window.open(google_search);
	}
}
</script>

<form name="search" align="center">
<input name="text" type="text" size="30">
<input name="button1" type="button" id="button1" value="百度搜索" onclick="baidu()">
<input name="button2" type="button" id="button2" value="谷歌搜索" onclick="google()">
</form>
