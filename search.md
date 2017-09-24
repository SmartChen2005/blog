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

<center>
<form name="search" align="center">
<input name="text" type="text" size="35">
<input name="button1" type="button" id="button1" value="百度一下" onclick="baidu()">
<input name="button2" type="button" id="button2" value="谷歌两下" onclick="google()">
<center>无法使用谷歌搜索？<a href="http://chenhongyi.cc/blog/2017/06/10/Google%E8%AE%BF%E9%97%AE%E5%8A%A9%E6%89%8B/">>>>点我<<<</a></center>
</form>
</center>

<br>
<div class="bdsharebuttonbox"><a href="#" class="bds_more" data-cmd="more"></a><a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a><a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a><a href="#" class="bds_renren" data-cmd="renren" title="分享到人人网"></a><a href="#" class="bds_fbook" data-cmd="fbook" title="分享到Facebook"></a><a href="#" class="bds_twi" data-cmd="twi" title="分享到Twitter"></a><a href="#" class="bds_linkedin" data-cmd="linkedin" title="分享到linkedin"></a><a href="#" class="bds_mail" data-cmd="mail" title="分享到邮件分享"></a><a href="#" class="bds_copy" data-cmd="copy" title="分享到复制网址"></a></div>
<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"欢迎访问陈弘毅的网站！","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"2","bdSize":"16"},"share":{},"image":{"viewList":["qzone","tsina","tqq","renren","fbook","twi","linkedin","mail","copy"],"viewText":"分享到：","viewSize":"16"},"selectShare":{"bdContainerClass":null,"bdSelectMiniList":["qzone","tsina","tqq","renren","fbook","twi","linkedin","mail","copy"]}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];</script>
