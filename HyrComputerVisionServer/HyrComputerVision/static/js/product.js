function checkImageSize(img){
	
	var max = (img.width > img.height? img.width:img.height);
	
	
    if(max > 500){
    	if(img.width == max){
    		img.width = "500";
    		img.height = img.height*500/max;
   		}else{
   			img.height = "500";
   			img.width = img.width*500/max;
   		}
    }
    
    if(img.height < 500){
		img.style.marginTop = String((500-img.height)/2.)+"px";
	}
    return img;
}

function clickSubmit(product_name){
	var urlNode = document.getElementById("imageURL");
	var img = document.createElement("img");
	img.src = urlNode.value;
	urlNode.value = "";
	setDetectImage(img, product_name);
}

function getMainEmotion(socres){			   
	var list = [socres.happiness, socres.surprise, socres.sadness, socres.neutral];
	var maxScores = 0;
	var resIdx = 0;
	for(var i = 0; i < 4; i++){
		if(maxScores < list[i]){
			maxScores = list[i];
			resIdx = i;
		}
	}
	return ["hapiness", "surprise", "sadness", "neutral"][resIdx];
}

function drawFaceRectEmotion(data, showDiv, img){
	$.each(data, function (i, item){
		var faceRectDiv = document.createElement("div");
    	showDiv.appendChild(faceRectDiv);
    	//画人脸框

    	faceRectDiv.style.border = "#00FFFF 2px solid";
    	faceRectDiv.style.position = "absolute";
    	var top = item['face_rectangle'].top + (500-img.height)/2;
    	faceRectDiv.style.top = top + "px";
    	var left = item['face_rectangle'].left + (500-img.width)/2;

		faceRectDiv.style.left = left + "px";
    	faceRectDiv.style.width = item['face_rectangle'].width + "px";
    	faceRectDiv.style.height = item['face_rectangle'].height + "px";

    	//写情绪得分的框
    	var emotionDiv = document.createElement("div");
    	showDiv.appendChild(emotionDiv);
    	emotionDiv.style.width = "150px";
    	emotionDiv.style.height = "100px";
    	emotionDiv.style.background = "gray";
    	emotionDiv.style.color = "white";
    	emotionDiv.style.position = "absolute";
    	emotionDiv.style.left = (left - 150) + "px";
    	emotionDiv.style.top = top + "px";
    	emotionDiv.style.display = "none";
    	emotionDiv.style.paddingTop = "10px";
    	emotionDiv.innerHTML = "happiness: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + item['scores'].happiness.toFixed(3) + "<br>" +
    							"sadness: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" +item['scores'].sadness.toFixed(3) + "<br>" + 
    							"neutral: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + item['scores'].neutral.toFixed(3)  + "<br>" +
    							"surprise: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + item['scores'].surprise.toFixed(3) ;
    	//写主要情绪的框
    	var mainEmotionDiv = document.createElement("div");
    	showDiv.appendChild(mainEmotionDiv);
    	mainEmotionDiv.style.width = "100px";
    	mainEmotionDiv.style.height = "30px";
    	mainEmotionDiv.style.background = "gray";
    	mainEmotionDiv.style.color = "white";
    	mainEmotionDiv.style.position = "absolute";
    	mainEmotionDiv.style.left = left+"px";
    	mainEmotionDiv.style.top = (top-30) +"px";
    	mainEmotionDiv.style.display = "none";
    	mainEmotionDiv.innerHTML = getMainEmotion(item['scores']);
    	faceRectDiv.onmouseover = function(){
    		emotionDiv.style.display = "block";
    		mainEmotionDiv.style.display = "block";
    	}
    	
    	faceRectDiv.onmouseout = function(){
    		emotionDiv.style.display = "none";
    		mainEmotionDiv.style.display = "none";
    	}
	});
}


function drawFace(data, showDiv, img){
	
	$.each(data, function (i, item){
		var faceRectDiv = document.createElement("div");
	    showDiv.appendChild(faceRectDiv);
	    //画人脸框
	    faceRectDiv.style.border = "#00FFFF 2px solid";
	    faceRectDiv.style.position = "absolute";
		var top = item['face_rectangle'].top + (500-img.height)/2;
	    faceRectDiv.style.top = top + "px";
		var left = item['face_rectangle'].left + (500 - img.width) / 2;
	
		faceRectDiv.style.left = left + "px";
		faceRectDiv.style.width = item['face_rectangle'].width + "px";
		faceRectDiv.style.height = item['face_rectangle'].height + "px";
		
		for (var i = 0; i < item.landmarks.length; i++){
			var pointDiv = document.createElement("div");
	    	showDiv.appendChild(pointDiv);
		    //画点
		    pointDiv.style.border = "red 1px solid";
		    pointDiv.style.position = "absolute";
			var top = item.landmarks[i][1] + (500-img.height)/2;
		    pointDiv.style.top = top + "px";
			var left = item.landmarks[i][0] + (500 - img.width) / 2;
			pointDiv.style.left = left + "px";
			pointDiv.style.width = "1px";
			pointDiv.style.height =  "1px";
		}
	});
}

function getFaceFormatStr(data){
	var res = "[\n";
	$.each(data, function (i, item){
		res += "  {  \n    \"face_rectangle\":{\n" + 
		"      \"top\":" + item['face_rectangle'].top + ",\n" + 
		"      \"left\":" + item['face_rectangle'].left + ",\n" + 
		"      \"width\":" + item['face_rectangle'].width + ",\n" + 
		"      \"height\":" + item['face_rectangle'].height + "\n" + "    },\n" +
		"    \"landmarks\":[\n      ";
		for (var i = 0; i < item.landmarks.length; i++){
			res += "[" + item.landmarks[i] +"]";
			if(i != item.landmarks.length-1){
				res += ", ";
			}else{
				res += "\n";
			}
			if((i+1)%5 == 0){
				res += "\n      ";
			}
		}
		res += "  ]\n";
		
	});
	res += "]";
	return res;
}

function setDetectImageByURL(url, data, product_name){
	var showDiv = document.getElementById("show_"+ product_name + "_image");
   	showDiv.innerHTML = "";
   	var img = document.createElement("img");
   	img.src=url;
   	img.onload = function(){
   		img = checkImageSize(img);
    	showDiv.appendChild(img);
    	if(product_name == "emotion"){
    		drawFaceRectEmotion(data, showDiv, img);
    	}
    	if(product_name == "face"){
    		drawFace(data, showDiv, img);
    	}
    	
   	}
	
}

function getEmotionFormatStr(data){
	var res = "[\n";
	$.each(data, function (i, item){
		res += "  {  \n    \"face_rectangle\":{\n" + 
		"      \"top\":" + item['face_rectangle'].top + ",\n" + 
		"      \"left\":" + item['face_rectangle'].left + ",\n" + 
		"      \"width\":" + item['face_rectangle'].width + ",\n" + 
		"      \"height\":" + item['face_rectangle'].height + "\n" + "    },\n" +
		"    \"socres\":{\n" +
		"      \"hapiness\":" + item['scores'].happiness + ",\n" +
		"      \"neutral\":" + item['scores'].neutral + ",\n" +
		"      \"sadness\":" + item['scores'].sadness + ",\n" +
		"      \"surprise\":" + item['scores'].surprise + "\n" + "    }\n"+
		"  }";
		if(i != data.length-1){
			res += ",\n";
		}else{
			res += "\n";
		}
	});
	
	res += "]"
	return res;
}

function getFormatStr(data, product_name) {
	if(product_name == "emotion"){
		return getEmotionFormatStr(data);
	}
	if(product_name == 'face'){
		return getFaceFormatStr(data);
	}
	return "\n\n该功能正在建设之中\n\n";
}

function setJsonDiv(data, product_name){
	var context = $("<pre>JSON:\n" + getFormatStr(data, product_name) + "</pre>");
	var show_json = $("#" + product_name + "_show_json");
	show_json.html("");
	show_json.append(context);
}

function setDetectImage(obj, product_name){
   	
	var jsonData = $.toJSON({
    	url:obj.src
    });

    $.post(server_url+"/"+product_name,  jsonData,
    	function(data, status){
    		setDetectImageByURL(obj.src, data, product_name);
	    	setJsonDiv(data, product_name);
    				
    	}, 'json');
}


