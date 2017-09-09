---
layout: page
title: "Smart Search"
description: "Smart Chen的私人搜索平台"
header-img: "img/sxl.png"
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
</script>

<form name="search" align="center">
<input name="text" type="text" size="40">
<input name="button" type="button" id="button" value="搜索" onclick="baidu()">
</form>

<center><h6>Copyright 2017 by Smart Chen</h6></center>
