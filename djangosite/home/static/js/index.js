$('.left-bar-box,.right-bar-box').find('h1').hover(
function(e){
	var $target = $(e.target)
	$target.next('.bottom-line').stop(true,false).animate({
		'width':'90px'
	})
},
function(e){
	var $target = $(e.target)
	$target.next('.bottom-line').stop(true,false).animate({
		'width':'40px'
	})
})
$('.wechat').hover(
	function(){
		$('.qr-code').fadeIn(600)
	},
	function(){
		$('.qr-code').fadeOut(600)
	}
)