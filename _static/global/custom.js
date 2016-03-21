
$(".form-control").change(function(){
	
	cashexp=document.getElementById("id_CashQuantity").options[document.getElementById("id_CashQuantity").selectedIndex].value*CashPrice;
	$("#cashexp").html(cashexp);
	masonexp=document.getElementById("id_MasonMoneyQuantity").options[document.getElementById("id_MasonMoneyQuantity").selectedIndex].value*MasonMoneyPrice;
	$("#masonexp").html(masonexp);
	barnesexp=document.getElementById("id_BarnesNobleQuantity").options[document.getElementById("id_BarnesNobleQuantity").selectedIndex].value*BarnesNoblePrice;
	$("#barnesexp").html(barnesexp);
	fandangoexp=document.getElementById("id_FandangoQuantity").options[document.getElementById("id_FandangoQuantity").selectedIndex].value*FandangoPrice;
	$("#fandangoexp").html(fandangoexp);
	gapexp=document.getElementById("id_GapQuantity").options[document.getElementById("id_GapQuantity").selectedIndex].value*GapPrice;
	$("#gapexp").html(gapexp);
	
	total_expenditure=cashexp+masonexp+barnesexp+fandangoexp+gapexp;
	$("#totalexp").html(total_expenditure);
})

$(".input-group-addon").html("%")