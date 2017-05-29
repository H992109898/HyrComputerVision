var product_to_chinese = {"emotion":"表情识别", 
	"obj":"物品识别", "face":"人脸识别","carPlate":"车牌识别"};

var type_to_chinese = {"free":"免费", "standard":"标准"};

var product_to_int = {"emotion":0, 
	"obj":1, "face":2,"carPlate":3};

var type_to_int =  {"free":0, "standard":1};

var cur_product = null
var cur_type = null

function clickBuy(product, type){

	/*
		product(String):购买产品名称：face,carPlate,emotion,obj
		type(int): 购买产品类型:free, standard
	*/
			

	var limit = (type == "free"? "100次/月":"无限");
	var myDate = new Date();
	var curTime = myDate.toLocaleDateString();
	myDate.setDate(myDate.getDate()+30);
	var endTime = myDate.toLocaleDateString();

	var tr="<tr><td >类别：</td> <td >" + product_to_chinese[product] +
	"</td> </tr><tr><td >类型：</td> <td >" + type_to_chinese[type] + 
	"</td> </tr><tr><td >限制：</td> <td >" + limit+ 
	"</td> </tr><tr><td >购买时间：</td> <td >" + curTime +
	"</td> </tr><tr><td >到期时间：</td> <td >" + endTime +"</td> </tr>"
	$("#product_type_table").html("");
	$("#product_type_table").append(tr);
	cur_product = product;
	cur_type = type;
}

function click_comfirm(){
	/*
	 * 向服务器Post购买信息
	 * type: 免费：0， 标准：1
	 * standard：表情识别：0，物品识别：1，人脸识别：2，车牌识别：3
	 */
	var jsonData = $.toJSON({
    	username:$.cookie("username"),
    	product:product_to_int[cur_product],
    	type:type_to_int[cur_type]
    });

    $.post(server_url+"/buy_product", 
    	jsonData,
    	function(data, status){
    		if(data == 0){
    			alert("不可重复购买");
    		}else{
    			alert("购买成功，您可在我的账号查看");
    		}
    	},'json');
}

function setBuyRecord(){
	var formData = new FormData();
	formData.append("init_buy_record", true);
	formData.append("username", $.cookie("username"));
	$.ajax({
		type: "POST",
	    url: server_url+"/myaccount_server",
	    data: formData,
	    processData : false,  
	    cache: false,
	    //必须false才会自动加上正确的Content-Type   
	    contentType : false,
	    success:function(jsonData) {
	    	var json_array = $.parseJSON(jsonData);
	    	$.each(json_array, function (i, item){
	    		var tr="<tr><td>" +product_to_chinese[item.product]+ "</td><td>" + item.start_time +
	    		"</td><td>" + item.end_time +"</td><td>" + 
	    		{"free":item.left_times, "standard":"无限"}[item.type]+
	    		"</td><td>" + item.product_key + "</td></tr>";
				$("#personal_buy_table_body").append(tr);
    		
			});
     	},    
	});
}