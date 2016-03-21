function toDecimal(num) {
    return parseFloat(Math.round(num * 100) / 100).toFixed(1);
}

$(".form-control").change(function(){
	
	cashexp=document.getElementById("id_CashQuantity").options[document.getElementById("id_CashQuantity").selectedIndex].value*CashPrice;
	$("#cashexp").html(toDecimal(cashexp));
	masonexp=document.getElementById("id_MasonMoneyQuantity").options[document.getElementById("id_MasonMoneyQuantity").selectedIndex].value*MasonMoneyPrice;
	$("#masonexp").html(toDecimal(masonexp));
	barnesexp=document.getElementById("id_BarnesNobleQuantity").options[document.getElementById("id_BarnesNobleQuantity").selectedIndex].value*BarnesNoblePrice;
	$("#barnesexp").html(toDecimal(barnesexp));
	fandangoexp=document.getElementById("id_FandangoQuantity").options[document.getElementById("id_FandangoQuantity").selectedIndex].value*FandangoPrice;
	$("#fandangoexp").html(toDecimal(fandangoexp));
	gapexp=document.getElementById("id_GapQuantity").options[document.getElementById("id_GapQuantity").selectedIndex].value*GapPrice;
	$("#gapexp").html(toDecimal(gapexp));
	
	total_expenditure=cashexp+masonexp+barnesexp+fandangoexp+gapexp;
	$("#totalexp").html(toDecimal(total_expenditure));
})

$(".input-group-addon").html("%")