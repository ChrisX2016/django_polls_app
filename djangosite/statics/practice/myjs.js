
// $(function(){
// 		$("#panel1").hide(1000).show(1000).slideUp(1000).delay(200).slideDown(1000).fadeOut(1000).fadeToggle(1000);

// });

// $(function(){
// 	$('.btn-default').on('click',function(){
// 		$('#panel1').slideToggle(200);
// 	});
// })
// slideup slidedown



// $(function() {
// 	$('.btn-primary').on('click',function(){
// 		$('#panel2 .panel-body').html('123123');
// 	});
// });

// panel
$(function(){
	$('.btn').on('click',function(){
		var panelId = $(this).attr('data-panelid');
		$('#'+panelId).slideToggle(200);
	});
});

$(function(){
	$('.table-panel').on('click',function(){
		var tableToShow = $(this).attr('rel');
		$('table.active').fadeOut(200,function(){
			$(this).removeClass('active');
			$('#'+tableToShow).fadeToggle(200,function(){
				$(this).addClass('active');
			});
		});
		$('li.active').removeClass('active');

		$(this).addClass('active');

	});
});

// Carousel
function showChevron(){
	$('.carousel-control,.glyphicon.glyphicon-chevron-left,.glyphicon.glyphicon-chevron-right').fadeIn(500);
	$('li[data-target="#carousel-example-generic"]').slideToggle(200);
}

function hiddenChevron(){
	$('.carousel-control,.glyphicon.glyphicon-chevron-left,.glyphicon.glyphicon-chevron-right').fadeOut(500);
	$('li[data-target="#carousel-example-generic"]').slideToggle(200);
}

$(function(){
	$('.glyphicon.glyphicon-chevron-left,.glyphicon.glyphicon-chevron-right').hide(1000);
})

$(function(){
	$('#carousel-example-generic').on('mouseenter',showChevron()).on('mouseleave',hiddenChevron())
});


// olark
$(function(){
	$('.olark-button').on('click',function(){
		$(this).slideUp(200,function(){
			$('.olark-table').css('opacity', 0).slideDown(800).animate({ opacity: 1 },{ queue: false,duration:800});
		});
	});
});

$(function(){
	$('.glyphicon-chevron-down.olark-button-icon').on('click',function(){
		$('.olark-table').slideUp(500,function(){
			$('.olark-button').slideDown(200);
		})
	});
});

// navbar
var buttomHeight = 2 * $('.page-header').outerHeight(true) + $('.jumbotron').outerHeight() - parseInt($(".mynavbar").css("margin-top"));

$(function(){
	$(window).scroll(function(){
		if($(window).scrollTop() >= buttomHeight){
			$('.mynavbar').addClass("isStuck");

			$('.page-header.panel-page-header').css({"margin-top":"112px"});
		}
		else{
			$('.mynavbar').removeClass("isStuck");
			$('.page-header.panel-page-header').css({"margin-top":"40px"});
		}
	});
});

$(function(){
	var top;
	var buttonHeight = "0"+"px";
	var narvbarHeight = $('.page-header').outerHeight(true) + $('.jumbotron').outerHeight();
	var panelHeight = narvbarHeight + $('.page-header').outerHeight(true) + $('.mynavbar').innerHeight();
	var tableHeight = panelHeight + $('.page-header').outerHeight(true) + $('.mypanel').outerHeight();
	var carouselHeight = tableHeight + $('.page-header').outerHeight(true) + $('mytable').outerHeight();

	$(window).scroll(function(){
		top = $(window).scrollTop();
		if(top<narvbarHeight){
			$('.nav.navbar-nav li:eq(0)').addClass("active");
			$('.nav.navbar-nav li:not(:eq(0))').removeClass("active");
		}
		else if(top<panelHeight){
			$('.nav.navbar-nav li:eq(1)').addClass("active");
			$('.nav.navbar-nav li:not(:eq(1))').removeClass("active");
		}
		else if(top<tableHeight){
			$('.nav.navbar-nav li:eq(2)').addClass("active");
			$('.nav.navbar-nav li:not(:eq(2))').removeClass("active");
		}
		else if(top<carouselHeight){
			$('.nav.navbar-nav li:eq(3)').addClass("active");
			$('.nav.navbar-nav li:not(:eq(3))').removeClass("active");
		}
		else{
			$('.nav.navbar-nav li:eq(4)').addClass("active");
			$('.nav.navbar-nav li:not(:eq(4))').removeClass("active");
		}
	});

})
