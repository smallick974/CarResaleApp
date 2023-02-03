/* Method to get state list */
function getStateList(){
	let statelist = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli',
	'Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep',
	'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Pondicherry','Punjab','Rajasthan','Sikkim',
	'Tamil Nadu','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
	return statelist
}

function getTitleStatusList(){
	let titleStatusList = ['Clean','Lien','Missing','Parts Only','Rebuilt','Salvage']
	return titleStatusList
}

function getCarConditionList(){
	let carConditionList = ['Excellent','Fair','Good','Like New','Salvage']
	return carConditionList
}

function getCylinderList(){
	let cylinderList = ['1','2','3','4','5','6','7','8','9','10']
	return cylinderList
}

function getFuelList(){
	let fuelList = ['CNG','Diesel','Electric','LPG','Petrol']
	return fuelList
}

function getTransmissionTypeList(){
	let transmissionTypeList = ['Automatic','Manual']
	return transmissionTypeList
}

function getDriveTypeList(){
	let driveTypeList = ['RWD','FWD','AWD','4WD']
	return driveTypeList
}

function getCarSizeList(){
	let carSizeList = ['Compact','Full-Size','Mid-Size','Sub-Compact']
	return carSizeList
}

function getCarTypeList(){
	let carTypeList = ['Cabriolet','Campervan','Convertible','Coupe','Hatchback','Hybrid','Limousine','Micro','Minivan','MUV','Pickup','Sedan','SUV','Wagon']
	return carTypeList
}

/* Allow only character in name field */
function validateName(event){
	if(!(/[a-z]|[A-Z]/g).test(event.key)) 
		event.preventDefault();
}

/* Method to navigate check validation and navigate to next page */
function navigateToAddress() {
	$("#txt_renter_password").prop('required',false);
	$("#txt_email_id1").prop('required',false);
    $("#txt_password1").prop('required',false);	
	isvalid = checkFormValidity('signup-validation')
	if(isvalid){
	    document.getElementById("step2").classList.add("completed")
    	document.getElementById("personal_info").classList.add("hide-element")
    	document.getElementById("address_info").classList.remove("hide-element");
    	document.getElementById("sign-in").classList.add("hide-element");
    	document.getElementById("step3").classList.remove("completed")
    	document.getElementById("step-completed").innerHTML = '3';
    	
    	/*set required fields for address page */
    	$("#txt_address1").prop('required',true);
    	$("#txt_city").prop('required',true);
    	$("#txt_state").prop('required',true);
    	$("#txt_zip").prop('required',true);
    	$("#txt_country").prop('required',true);
    	
    	/*populate states */
    	states = getStateList();
    	states.forEach((item) => {
			$('#txt_state').append('<option value="' + item + '">' + item + '</option>');
		})
    }
}

/*Method to navigate to Sign up page when new user sign ups*/
function navigateToSignIn(){
	isvalid = checkFormValidity('signup-validation')
	if(isvalid){
		document.getElementById("step2").classList.add("completed")
    	document.getElementById("step3").classList.add("completed")
    	document.getElementById("step-completed").innerHTML = '&#x2714';
    	document.getElementById("address_info").classList.add("hide-element");
    	document.getElementById("sign-in").classList.remove("hide-element");
    	$("#txt_renter_password").prop('required',true);
    	$("#txt_email_id1").prop('required',true);
    	$("#txt_password1").prop('required',true);	
	}
    
}

/* Method to navigate to Personal info page when new user sign ups */
function navigatePersonalInfo(){
    document.getElementById("step2").classList.remove("completed")
    document.getElementById("personal_info").classList.remove("hide-element")
    document.getElementById("address_info").classList.add("hide-element");
    document.getElementById("sign-in").classList.add("hide-element");
    
    /*remove required fields on previous page */
    $("#txt_address1").prop('required',false);
    $("#txt_city").prop('required',false);
    $("#txt_state").prop('required',false);
    $("#txt_zip").prop('required',false);
    $("#txt_country").prop('required',false);
    $("#txt_password1").prop('required',false);
}

/* Set default visibilit of sign up pages */
function setDefaultVisibility(){
    document.getElementById("personal_info").classList.remove("hide-element")
    document.getElementById("address_info").classList.add("hide-element");
    document.getElementById("step2").classList.remove("completed")
    document.getElementById("step3").classList.remove("completed")
    document.getElementById("step-completed").innerHTML = '3';
    document.getElementById("sign-in").classList.add("hide-element");
}

/* Method to Resend otp if not received */
function submitResendOtp(){
    document.getElementById("resend_otp").classList.remove("hide-element");
    document.getElementById("btn_sendotp").innerHTML = "Submit";
}

/* Method to send otp to user */
function sendOtp(){
    let user_emailid = $('#txt_email_id').val()
	jQuery.ajax({
		url:'/ResetPassword',
		data: {'user_emailid':user_emailid},
		dataType: 'json',
		success: function(response){
			if(typeof(response) == 'object' && 'ERROR' in response){
				$('#reset_error_message').html(response['ERROR'])
			}
			else{
				if(response.otp!='' && response.otp!=undefined && response.otp!='undefined' && response.otp!=null){
					$("#reset_error_message").html('')
					document.getElementById("otpdiv").classList.remove("hide-element")
					document.getElementById("txt_email_id").disabled = "true"
					$("#txt_otp").prop('required',true);
					$("#txt_otp_hidden").val(response.otp)
					submitResendOtp()
				}
			}
		} 
	}); 
}

/* Method to reset Password */
function resetPassword(){
	$('#txt_email_id').prop('disabled',false)
		jQuery.ajax({
    		type: "POST",
			url:'/UpdatePassword',
			data : $('#reset_password_form').serialize(),
			dataType: 'json',
			success: function (response){
					if(typeof(response) == 'object' && 'ERROR' in response){
  						$('#reset_error_message').html('Error in updating Password')	
					}
					else{
						window.location.href = response
					}
				}
		});
}

/* Method to get wishlisted cars ids */
function getWishlistedCars(wishlisted_cars){
	const wishlisted_car_ids_set = new Set();
	if(wishlisted_cars.length>0){
		for(index=0; index < wishlisted_cars.length; index++){
			wishlisted_car_ids_set.add(wishlisted_cars[index][0])
		}
	}
	return wishlisted_car_ids_set;
}

function displayData(car_list,wishlisted_car_ids_set,sessionvar){
	var htmldata = '<div class="row">'
	if(car_list.length > 0){
		for (index =0; index < car_list.length;){
			var car = car_list[index]
			if(index!=0 && index%4==0){
				htmldata = htmldata+'<div class="row">'
			}
			for(i = 0;i<4;i++){
				if(index<car_list.length){
					var car = car_list[index]
					cars.manufacturer = car[1]
					cars.model = car[2]
					cars.buildyear = car[5]
					cars.condition = car[6]
					cars.cylinder = car[7]
					cars.fueltype = car[8]
					cars.drivetype = car[9]
					cars.state = car[10]
					cars.size = car[11]
					cars.price = car[3]
					cars.manufacturerId = car[12]
					cars.modelId = car[14]
					modelname = car[2].replaceAll(' ','_')
					htmldata= htmldata+'<div class="col-3">'+
  						'<div class="card">'+
  						"<img style='height:300px' class='card-img-top' src='/static/CarImages/"+modelname+"/"+car[4]+"'>"+
							'<div class="card-body">'+
  								'<h4 class="card-title">'+car[1]+'</h4>'+
  								'<p class="card-text">'+car[2]+'</p>'+
  								'<p class="card-text"><b>Price: ₹ '+car[3]+'</b></p>'+
  								'<a href="/ViewCar/'+car[0]+'" class="btn btn-primary div-style" target="_blank">View Car</a>'
  						if(wishlisted_car_ids_set.has(car[0])){
  							htmldata = htmldata+'<a href="/UpdateWishlist/'+car[0]+'" class="btn btn-primary div-style disabled">Wishlisted</a>'
  						}
  						else{
							if('userData' in sessionvar)
								htmldata= htmldata+'<a href="/UpdateWishlist/'+car[0]+'" class="btn btn-primary div-style">Wishlist</a>'
							else
  								htmldata = htmldata+'<a href="#login" class="btn btn-primary div-style" data-bs-toggle="modal">Wishlist</a>'
  						}
					htmldata=htmldata+'</div>'+
						'</div>'+
						'</div>'
						index++
				}
			}
	    	htmldata = htmldata+'</div>'
		}
	}
	else{
		htmldata = htmldata+'<div class="text-center"><h4>No matching cars found! Please refine your search criteria.</h4></div>'+'</div>'
	}
    $('#carcard').html(htmldata)
}

function clearFilters(){
	$('.searchdata:checkbox:checked').each(function () {
		this.checked = false
    });
    
    lstmanufacture = []
    lstmodel = []
    lstyear = []
    lstcondition = []
    lstcylinder = []
    lstfueltype = []
    lstdrivetype = []
    lststate = []
    lstsize = []
    
    minval = $('#hiddenminpricevalue').val()
    maxval = $('#hiddenmaxpricevalue').val()
    $('#minpricevalue').val(minval)
    $('#maxpricevalue').val(maxval)
    $('#minpricerange').val(minval)
    $('#maxpricerange').val(maxval)
    $('#maxval1').html= minval;
    $('#maxpricerange').attr("min",minval)
    $('minval2').html= maxval;
   	$('#minpricerange').attr("max",maxval)
}

/* Method to check if form data is valid */
function checkFormValidity(validation){
	isvalid = true
	const forms = document.querySelectorAll('.'+validation);
	Array.prototype.slice.call(forms).forEach((form) => {
		if(!form.checkValidity()){
			isvalid = false
		}
		form.classList.add('was-validated');
	},false)
	return isvalid;	
}

function checkYearValidation(value){
	if(value > new Date().getFullYear()){
		document.getElementById('txt_build_year').setCustomValidity('Valid Build Year is required')
	}
	else{
		document.getElementById('txt_build_year').setCustomValidity('')
	}
}	

/* Method for Login into the system */
function login(){
	isvalid = checkFormValidity('login-validation');
	if(isvalid){
		jQuery.ajax({
    		type: "POST",
			url:'/Welcome',
			data : $('#login_form').serialize(),
			dataType: 'json',
				success: function (response){
					if(typeof(response) == 'object' && 'Error' in response){
  						$('#login_error_message').html(response['Error'])	
					}
					else{
						window.location.href = response
					}
				}
		});
	}
}

/* Method for signup new user into the system */
function usersignup(){
	isvalid = checkFormValidity('signup-validation');
	if(isvalid){
		jQuery.ajax({
    		type: "POST",
			url:'/Home',
			data : $('#signup_form').serialize(),
			dataType: 'json',
				success: function (response){
					if(typeof(response) == 'object' && 'ERROR' in response){
  						$('#error_message').html(response['ERROR'])	
					}
					else{
						window.location.href = response
					}
				}
		});
	}
}

/* Method to update profile */
function updateProfile(){
	let isvalid = checkFormValidity('profile-validation')
	if(isvalid){
		jQuery.ajax({
    		type: "POST",
			url:'/ProfileUpdate',
			data : $('#profile_form').serialize(),
			dataType: 'json',
				success: function (response){
					if(typeof(response) == 'object' && 'ERROR' in response){
  						$('#profile_error_message').html(response['ERROR'])	
					}
					else{
						window.location.href = response
					}
				}
		});
	}
}

function updateUserProfile(){
	isvalid = checkFormValidity('update-user-profile-validation')
	if(isvalid){
		let userFormData = new FormData()
		userFormData.append("txt_userfirstname", $("#txt_userfirstname").val())
		userFormData.append("txt_userlastname", $("#txt_userlastname").val())
		userFormData.append("txt_userphone_no", $("#txt_userphone_no").val())
		userFormData.append("txt_useremail_id1", $("#txt_useremail_id1").val())
		userFormData.append("userId", $("#txt_userId").val())
		jQuery.ajax({
    		type: "POST",
			url:'/ProfileUpdate',
			data : userFormData,
			contentType: false,
			processData: false,
			dataType: 'json',
				success: function (response){
					if(typeof(response) == 'object' && 'ERROR' in response){
  						$('#userprofile_error_message').html(response['ERROR'])	
  						$('#user_message').html('')
					}
					else{
						$('#userprofile_error_message').html('')	
						$('#user_message').html('Profile details updated successfully!')
					}
				}
		});
	}
}

/* Method to check Password validity */
function checkPasswordValidity(txtPassword,lowercase,uppercase,number,password,special_char){
    let lowerCaseLetters = /[a-z]/g;
    let isPasswordValid= true
    if(txtPassword.value.match(lowerCaseLetters)) {
		lowercase.classList.remove("invalid");
        lowercase.classList.add("valid");
                isPasswordValid = isPasswordValid == false ? false: true
            } else {
                lowercase.classList.remove("valid");
                lowercase.classList.add("invalid");
                isPasswordValid = false
            }
            let upperCaseLetters = /[A-Z]/g;
            if(txtPassword.value.match(upperCaseLetters)) {
                uppercase.classList.remove("invalid");
                uppercase.classList.add("valid");
                isPasswordValid = isPasswordValid == false ? false: true
            } else {
                uppercase.classList.remove("valid");
                uppercase.classList.add("invalid");
                isPasswordValid = false
            }
            let numbers = /[0-9]/g;
            if(txtPassword.value.match(numbers)) {
                number.classList.remove("invalid");
                number.classList.add("valid");
                isPasswordValid = isPasswordValid == false ? false: true
            } else {
                number.classList.remove("valid");
                number.classList.add("invalid");
                isPasswordValid = false
            }
            let special = /[!@#$&*]/g;
            if(txtPassword.value.match(special)) {
                special_char.classList.remove("invalid");
                special_char.classList.add("valid");
                isPasswordValid = isPasswordValid == false ? false: true
            } else {
                special_char.classList.remove("valid");
                special_char.classList.add("invalid");
                isPasswordValid = false
            }
            if(txtPassword.value.length >= 8) {
                password.classList.remove("invalid");
                password.classList.add("valid");
                isPasswordValid = isPasswordValid == false ? false: true
            } else {
                password.classList.remove("valid");
                password.classList.add("invalid");
                isPasswordValid = false
            }
	return isPasswordValid;
}

/* Method to upload new car */
function uploadCar(){
	let isvalid = checkFormValidity('upload-car-validation');
	$('#newcar_error_message').html('')
	if(isvalid){
		var carformdata = new FormData();
		var carfiles = document.querySelectorAll('.carimage-file');
		var uploaded_files_count = 5;
		var validfiles = true;
		for(var i=0; i<carfiles.length; i++){
			if(carfiles[i].files[0] === undefined)
				uploaded_files_count--;
			else{
				var validextension = /(\.jpg|\.jpeg|\.png)$/i;
				if (!validextension.exec(carfiles[i].value)) {
                	var imgfile = document.querySelector('.'+carfiles[i].id)
                	imgfile.classList.add('invalid-image-border')
                	validfiles = false
            	}
            	else{ 
					carformdata.append("files", carfiles[i].files[0]);
				}
			}
		}
		if(uploaded_files_count === 0)
			$('#newcar_error_message').html('No image selected for uploading')
		else if(!validfiles)
			$('#newcar_error_message').html('Select valid files format (.png/.jpg/.jpeg)')
		else{
			$('#newcar_error_message').html('')
			var cardata = document.querySelectorAll('.car-data')
			for(var i=0; i<cardata.length; i++){
				carformdata.append(cardata[i].id,cardata[i].value);
			}
			carformdata.append("form",$('#uploadcar_form').serialize())
			jQuery.ajax({
    			type: "POST",
				url:'/UploadCar',
				data : carformdata,
				contentType: false,
				processData: false,
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#newcar_error_message').html(response['ERROR'])	
						}
						else{
							window.location.href = response
						}
					}
			});
		}
	}	
}

function estimatePrice(){
	let isvalid = checkFormValidity('upload-car-validation');
	$('#newcar_error_message').html('')
	if(isvalid){
				jQuery.ajax({
    			type: "POST",
				url:'/EstimatePrice',
				data : $('#uploadcar_form').serialize(),
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#newcar_error_message').html(response['ERROR'])	
						}
						else{
							let estimatedprice = Math.abs(response)
							let minprice = Math.round(parseInt(estimatedprice) - (estimatedprice*(10/100)));
							let maxprice = Math.round(parseInt(estimatedprice) + (estimatedprice*(10/100)));
							$('#txt_minestimatedprice').html(minprice)
							$('#txt_maxestimatedprice').html(maxprice)
							$('#txt_carprice').attr('min',minprice)
							$('#txt_carprice').attr('max',maxprice)
							$('#txt_carprice').attr('value',response)
							$('#txt_EstimatedPrice').val(response)
							$('#estimatedpricediv').removeClass('hide-element')
							$('#btnSaveCar').removeAttr('disabled')
						}
					}
			});
	}
}

function estimatePriceForUpdate(){
	let isvalid = checkFormValidity('update-car-validation');
	$('#newcar_error_message').html('')
	if(isvalid){
				jQuery.ajax({
    			type: "POST",
				url:'/EstimatePrice',
				data : $('#update_car_form').serialize(),
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#newcar_error_message').html(response['ERROR'])	
						}
						else{
							let estimatedprice = Math.abs(response)
							let minprice = Math.round(parseInt(estimatedprice) - (estimatedprice*(10/100)));
							let maxprice = Math.round(parseInt(estimatedprice) + (estimatedprice*(10/100)));
							$('#txt_minestimatedprice').html(minprice)
							$('#txt_maxestimatedprice').html(maxprice)
							$('#txt_carprice').attr('min',minprice)
							$('#txt_carprice').attr('max',maxprice)
							$('#txt_carprice').attr('value',response)
							$('#txt_EstimatedPrice').val(response)
							$('#estimatedpricediv').removeClass('hide-element')
							$('#btnUpdateCar').removeAttr('disabled')
						}
					}
			});
	}
	else{
		$('#btnUpdateCar').addAttr('disabled',true)
	}
}


function displaySelectedCarPrice(range){
	$('#txt_EstimatedPrice').val(range.value)
}

function loadCarImageThumbnail(element,imgcar,thumbnail){
	const carimage = element.files[0];
	if (carimage){
		let fileReader = new FileReader();
		fileReader.onload = (event)=>{
			$(imgcar).attr('src', event.target.result);
			$(imgcar).addClass('image-class')
			$(thumbnail).attr('src', event.target.result);
			$(thumbnail).addClass('image-thumbnail');
			$(thumbnail).removeClass('invalid-image-border')
		}
		fileReader.readAsDataURL(carimage);
	}
}

function removeCarImage(image,thumbnail,inputfield){
        	$(image).attr('src', '/static/imagebackground.jpg');
        	$(thumbnail).attr('src', '/static/image_upload.png');
        	$(thumbnail).removeClass('invalid-image-border')
			$(inputfield).val('')
        }

function validateBuyer(carid){
	isvalid = checkFormValidity('sold-out-validation_'+carid);	
	if(isvalid){
		jQuery.ajax({
    			type: "GET",
				url:'/SearchAndUpdateRecords',
				data : {'value':$("#txt_contact_"+carid).val(),
				        'table_name':'usercontact'},
				dataType: 'json',
					success: function (response){
						console.log(response)
						if(typeof(response) == 'object' && 'ERROR' in response){
							$('#txt_contact_'+carid).removeAttr('disabled')
							$('#btnUpdateSP_'+carid).attr('disabled')
  							$('#sold_out_error_div_'+carid).html(response['ERROR'])
						}
						else if (response.result == null ){
							$('#txt_contact_'+carid).removeAttr('disabled')
							$('#sold_out_error_div_'+carid).html('')
							$('#btnUpdateSP_'+carid).attr('disabled')
							$('#txt_username_'+carid).html("<div style='color:red'>Contact does not exists</div>")
						}
						else{
							console.log('user id')
							console.log(response.result[0][3])
							$('#sold_out_error_div_'+carid).html('')
							$('#txt_contact_'+carid).attr("disabled", "disabled")
							$('#txt_username_'+carid).html("<div style='color:black'>Buyer's Name: "+response.result[0][1]+' '+response.result[0][2]+"</div>")
							$('#txt_userid_'+carid).val(response.result[0][3])
							$('#btnUpdateSP_'+carid).removeAttr('disabled')
						}
						
						
					}
			});	
	}
}        
function updateSellingPrice(carid,estimatedprice){
	isvalid = checkFormValidity('sold-out-validation_'+carid);	
	if(isvalid){
		var carformdata = new FormData();
		carformdata.append("soldout","true")
		var sprice = document.getElementById("txt_sellingprice_"+carid).value
		let minprice = Math.round(parseInt(estimatedprice) - (estimatedprice*(10/100)));
		console.log(minprice)
		let maxprice = Math.round(parseInt(estimatedprice)+(estimatedprice*(10/100)));
		console.log(maxprice)
		if((sprice < minprice) || (sprice > maxprice)){
			isvalid = false
			$('#sold_out_error_div_'+carid).html('Price should be within range '+minprice + ' and '+maxprice)
		}
		else{
			isvalid = true
			$('#sold_out_error_div_'+carid).html('')
			console.log($('#txt_userid_'+carid).val())
			document.getElementById('txt_sellingprice_'+carid).setCustomValidity('')
			carformdata.append("txt_sellingprice",sprice)
			carformdata.append("txt_purchaseduid",$('#txt_userid_'+carid).val())
			/jQuery.ajax({
    			type: "POST",
				url:'/UpdateCar/'+carid,
				data : carformdata,
				contentType: false,
				processData: false,
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#sold_out_error_div').html(response['ERROR'])	
						}
						else{
							window.location.href = response
						}
					}
			});
		}
	}
	
}

function getSellerDetails(userId){
	jQuery.ajax({
    			type: "GET",
				url:'/SellerDetails/'+userId,
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#sold_out_error_div').html(response['ERROR'])	
						}
						else{
							var htmldata = '<h5>Name: '+response[0][0]+'&nbsp'+response[0][1]+'</h5>'
							htmldata = htmldata + '<br/> Contact at '+response[0][3]+'<br/> or Email at '+response[0][2]
							$('#sellerDetails').html(htmldata)
							$('#contact_seller_modal').modal('show');
						}
					}
			});	
}


function updateCar(carid){
	let isvalid = checkFormValidity('update-car-validation');
	$('#update_error_message').html('')
	if(isvalid){
		var carformdata = new FormData();
		var carfiles = document.querySelectorAll('.car-image-class');
		var carfiles1 = document.querySelectorAll('.carimage-file1');
		var uploaded_files_count = 5;
		var validfiles = true;
		for(var i=0; i<carfiles.length; i++){
			if(carfiles[i].getAttribute("src") === '/static/image_upload.png')
				uploaded_files_count--;
			else{
				var validextension = /(\.jpg|\.jpeg|\.png)$/i;
				if (!validextension.exec(carfiles[i].getAttribute("src")) && !validextension.exec(carfiles1[i].value)) {
                	var imgfile = document.querySelector('.'+carfiles1[i].id)
                	imgfile.classList.add('invalid-image-border')
                	validfiles = false
            	}
            	else if(carfiles1[i].files[0] != undefined){
					carformdata.append("files", carfiles1[i].files[0]);
				}
				else{
					carformdata.append("files", carfiles[i].getAttribute("src"));
				}
			}
		}
		if(uploaded_files_count === 0)
			$('#update_error_message').html('No image selected for uploading')
		else if(!validfiles)
			$('#update_error_message').html('Select valid files format (.png/.jpg/.jpeg)')
		else{
			$('#update_error_message').html('')
			var cardata = document.querySelectorAll('.car-data')
			console.log(cardata)
			for(var i=0; i<cardata.length; i++){
				carformdata.append(cardata[i].id,cardata[i].value);
			}
			console.log('carform data')
			console.log(carformdata)
			carformdata.append("form",$('#update_car_form').serialize())
			jQuery.ajax({
    			type: "POST",
				url:'/UpdateCar/'+carid,
				data : carformdata,
				contentType: false,
				processData: false,
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#update_error_message').html(response['ERROR'])	
						}
						else{
							window.location.href = response
						}
					}
			});
		}
	}
}

function saveManufacturerModel(){
	let manufacturerName = ($("#txt_manufacturer_name").val()=='')?$("#txt_new_Manufacturer").val():$("#txt_manufacturer_name").val()
	let modelnameList = []
	let modelname = $("#txt_new_model").val()
	modelnameList1 = modelname.split(/\r?\n/)
	isValid = false
	modelnameList = modelnameList1.filter(modelname => {
  		return modelname !== '';
	});
	if(manufacturerName == ''){
		$("#add_new_model_errormsg").html('Please select existing manufacturer or add new manufacturer')
	}
	else if(modelname == ''){
		$("#add_new_model_errormsg").html('Model name is required')
	}
	else if(modelnameList.length>0){
		let duplicate = arr => arr.filter((item, index) => arr.indexOf(item) != index)
		duplicateModels = [...new Set(duplicate(modelnameList))]
		if(duplicateModels.length > 0){
			$("#add_new_model_errormsg").html('Please remove duplicate Models: '+duplicateModels)
		}
		else{
			isValid = true
		}
	}
	if($("#txt_new_Manufacturer").val() != '' && isValid){
		$("#add_new_model_errormsg").html('')
		jQuery.ajax({
    			type: "GET",
				url:'/SearchAndUpdateRecords',
				data : {'value':$("#txt_new_Manufacturer").val(),
				        'table_name':'manufacturer'},
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#add_new_model_errormsg').html(response['ERROR'])	
						}
						else if (response.result.length > 0 ){
							$("#add_new_model_errormsg").html('Manufacturer already exists')
						}
						else{
							insertNewManufacturerModel(manufacturerName,modelnameList)
						}
					}
			});	
	}
	if($("#txt_manufacturer_name").val()!='' && isValid){
		$("#add_new_model_errormsg").html('')
		jQuery.ajax({
			type: "GET",
			url:'/SearchAndUpdateRecords',
			data : {'value':$("#txt_manufacturer_name").val(),
				     'table_name':'model'},
			dataType: 'json',
			success: function (response){	
				if(typeof(response) == 'object' && 'ERROR' in response){
  					$('#add_new_model_errormsg').html(response['ERROR'])	
				}
				else if (response.result.length > 0 ){
					let existingModelList = []
					for(let index = 0; index < response.result.length; index++){
						for(let m=0; m<modelnameList.length;m++){
							if(modelnameList[m] == response.result[index][2]){
								existingModelList.push(modelnameList[m])
							}
						}
					}
					if(existingModelList.length > 0){
						$("#add_new_model_errormsg").html('Model already exists '+existingModelList)
					}
					else{
						$("#add_new_model_errormsg").html('')
						insertNewManufacturerModel(manufacturerName,modelnameList)
					}
				}
			}
		});	
	}
}

function insertNewManufacturerModel(manufacturerName,modelnameList){
	let modelFormData = new FormData()
	modelFormData.append("manufacturerName",manufacturerName)
	modelFormData.append("modelList",modelnameList)
	modelFormData.append("actionType", $("#txt_manufacturer_name").val()==''?"MANUFACTURER_MODEL_INSERT":"MODEL_INSERT")
	$("#add_new_model_errormsg").html('')
	jQuery.ajax({
    	type: "POST",
		url:'/SearchAndUpdateRecords',
		data : modelFormData,
		contentType: false,
		processData: false,
		dataType: 'json',
		success: function (response){
			if(typeof(response) == 'object' && 'ERROR' in response){
  				$('#add_new_model_errormsg').html(response['ERROR'])	
			}
			else {
				window.location.href = response						
			}
		}
	});	
}

 
function saveColor(){
	let isvalid = checkFormValidity('new-model-color');
	if(isvalid){
		let colorList = []
		let colors = $("#txt_car_color").val()
		colorList1 = colors.split(/\r?\n/)
		colorList = colorList1.filter(colorname => {
  			return colorname !== '';
		});
		if(colorList.length > 0){
			let duplicate = arr => arr.filter((item, index) => arr.indexOf(item) != index)
			duplicateColors = [...new Set(duplicate(colorList))]
			if(duplicateColors.length > 0){
				$("#add_new_body_errormsg").html('Please remove duplicate Model colors: '+duplicateColors)
			}
			else{
				$("#add_new_body_errormsg").html('')
				let dupeColorList = []
				let existingColorList = []
				let e = document.getElementById('txt_modellist')
				let model_name = e.options[e.selectedIndex].text;
				let request = new Request("static/Car_Color.json");
				fetch(request)
					.then(function(response){
						return response.json()
				})
				.then(function(data){
					for (var index = 0; index < data[model_name]?.length; index++) {
						existingColorList.push(data[model_name][index])
   					}
   					if(existingColorList.length > 0){
						for(var i = 0; i< existingColorList.length; i++){
							for(var j = 0; j < colorList.length; j++){
								if(existingColorList[i].toLowerCase() == colorList[j].toLowerCase() && (!dupeColorList.includes(existingColorList[i]))){
									dupeColorList.push(existingColorList[i]);
								}
							}	
						}
					}
					if(dupeColorList.length > 0)
						$("#add_new_body_errormsg").html('Model already has these colors: '+dupeColorList)
					else{
						let colorFormData = new FormData()
						colorFormData.append("modelName",model_name)
						colorFormData.append("bodyColorList",colorList)
						colorFormData.append("actionType", "COLOR_INSERT")
						$("#add_new_body_errormsg").html('')
						jQuery.ajax({
    						type: "POST",
							url:'/SearchAndUpdateRecords',
							data : colorFormData,
							contentType: false,
							processData: false,
							dataType: 'json',
							success: function (response){
								if(typeof(response) == 'object' && 'ERROR' in response){
  									$('#add_new_body_errormsg').html(response['ERROR'])	
								}
								else {
									window.location.href = response						
								}
							}
						});
					}
				})
			}
		}
	}
}
 


$(document).ready(function(){
	
	/* Sign up modal popup validations */
	
    $("#signUp").on('shown.bs.modal', function(){
		setDefaultVisibility()
		/* Strong Password validations */
        let txtPassword = document.getElementById("txt_password1");
        txtPassword.onfocus = () => {
            document.getElementById("strong_password").style.display = "block";
        }
        txtPassword.onblur = () => {
            document.getElementById("strong_password").style.display = "none";
        }
        txtPassword.onkeyup = function() {
            let lowercase = document.getElementById("lowercase")
			let uppercase = document.getElementById("uppercase")
   	 		let number = document.getElementById("number")
    		let password = document.getElementById("password_length")
    		let special_char = document.getElementById("special_char")
            let isPasswordValid = checkPasswordValidity(txtPassword,lowercase,uppercase,number,password,special_char)
            
			if(!isPasswordValid){
            	$("#txt_renter_password").prop('disabled',true);
            	$("#txt_renter_password").val('');
            }
            else
            	$("#txt_renter_password").prop('disabled',false);
        }
        
        /* Re-enter password validations */
        document.getElementById("txt_renter_password").onkeyup = function() {
            let password1 = $('input[id=txt_password1]').val()
            let re_enter_password = $('input[id=txt_renter_password]').val()
            if(password1 == ''){
                $("#txt_password1").addClass("border-color");
            }
            if(re_enter_password == '' || password1 == re_enter_password){
                document.getElementById("password_not_match_span").innerText = "";
            }
            if(password1 != re_enter_password){
                document.getElementById("password_not_match_span").innerText = "Password doesn\'t match";
            }
            if(password1 == re_enter_password){
				$("#btn_signupsubmit").prop('disabled',false);
			}
			else{
				$("#btn_signupsubmit").prop('disabled',true);
			}
        }
		
		/**********NOT REQUIRED NEED TO CHECK */
        document.getElementById("btntogglepassword").onclick = () => {
            var txt_password = document.getElementById("txt_password1");
            if (txt_password.type === "password") {
                txt_password.type = "text";
                $("#btntogglepassword1").removeClass("glyphicon glyphicon-eye-close")
                $("#btntogglepassword1").addClass("glyphicon glyphicon-eye-open")
            } else if (txt_password.type === "text"){
                txt_password.type = "password";
                $("#btntogglepassword1").removeClass("glyphicon glyphicon-eye-open")
                $("#btntogglepassword1").addClass("glyphicon glyphicon-eye-close")
            }
        }

        document.getElementById("btntogglepassword2").onclick = () => {
            var txt_password = document.getElementById("txt_renter_password");
            if (txt_password.type === "password") {
                txt_password.type = "text";
                $("#btntogglepassword3").removeClass("glyphicon glyphicon-eye-close")
                $("#btntogglepassword3").addClass("glyphicon glyphicon-eye-open")
            } else if (txt_password.type === "text"){
                txt_password.type = "password";
                $("#btntogglepassword3").removeClass("glyphicon glyphicon-eye-open")
                $("#btntogglepassword3").addClass("glyphicon glyphicon-eye-close")
            }
        } 
        
            
    });
    
    $('#login').on('hidden.bs.modal', function () {
    	$('#login_error_message').html('')
    	$('#txt_email_id').val('')
    	$('#txt_password').val('')
	}); 
    
    /* Send OTP and reset password */
     $("#reset_password").on('shown.bs.modal', function(){
					
			document.getElementById("btn_sendotp").onclick = (event) => {
				if(event.target.innerHTML == 'Send OTP'){
					let isvalid = checkFormValidity('reset-validation')
					if(isvalid){
						sendOtp()						
					}
				}
				else if(event.target.innerHTML == 'Submit'){
					let otp = $('#txt_otp_hidden').val()
					let userotp = $('#txt_otp').val()
					if(otp != userotp)
						$('#reset_error_message').html('Invalid OTP!!!')
					else{
						$('#resetotpdiv').addClass("hide-element")
						$('#setpassworddiv').removeClass("hide-element")
						$('#txt_newpassword').prop('required',true)
						$("#reset_error_message").html('')
					}
				}
			}
			document.getElementById("resend_otp").onclick = () => {
				sendOtp()
			}
			let txt_newpassword = document.getElementById("txt_newpassword");
			txt_newpassword.onfocus = () => {
            	document.getElementById("strong_password1").style.display = "block";
        	}
        	txt_newpassword.onblur = () => {
            	document.getElementById("strong_password1").style.display = "none";
        	}
			txt_newpassword.onkeyup = function() {
				let lowercase = document.getElementById("lowercase1")
				let uppercase = document.getElementById("uppercase1")
   	 			let number = document.getElementById("number1")
    			let password = document.getElementById("password_length1")
    			let special_char = document.getElementById("special_char1")
            	let isPasswordValid = checkPasswordValidity(txt_newpassword,lowercase,uppercase,number,password,special_char)
            
				if(!isPasswordValid){
            		$("#txt_confirmnewpassword").prop('disabled',true);
            		$("#txt_confirmnewpassword").val('');
            	}
            	else
            		$("#txt_confirmnewpassword").prop('disabled',false);	
			}
			
			document.getElementById("txt_confirmnewpassword").onkeyup = function() {
            	let password1 = $('input[id=txt_newpassword]').val()
            	let re_enter_password = $('input[id=txt_confirmnewpassword]').val()
            	if(password1 == ''){
                	$("#txt_newpassword").addClass("border-color");
            	}
            	if(re_enter_password == '' || password1 == re_enter_password){
               	 	$("#reset_error_message").html('')
            	}
            	if(password1 != re_enter_password){
                	$("#reset_error_message").html("Password doesn\'t match")
            	}
            	if(password1 == re_enter_password){
					$("#btn_resetpassword").prop('disabled',false);
				}
				else{
					$("#btn_resetpassword").prop('disabled',true);
				}
        }
	});
	
	 $('#reset_password').on('hidden.bs.modal', function () {
		$('#txt_email_id').prop('disabled',false)
		$('#txt_email_id').val('')
    	$('#emaildiv').removeClass('hide-element')
    	$('#setpassworddiv').addClass('hide-element')
    	$('#pwd_reset_successfull').addClass('hide-element')
    	$('#resetotpdiv').removeClass('hide-element')
    	$('#otpdiv').addClass('hide-element')
    	$('#resend_otp').addClass('hide-element')
    	$('#btn_sendotp').html('Send OTP')
    	$('#txt_newpassword').val('')
    	$('#txt_confirmnewpassword').val('')
    	$('#txt_newpassword').prop('required',false)
    	$('#txt_confirmnewpassword').prop('required',false)
    	$('#txt_otp').val('')
    	$('#txt_otp_hidden').val('')
	}); 
  
  $("#txt_manufacturer").change(function(){
		let mname = $('#txt_manufacturer').val()
		if(mname == ''){
			$('#txt_model').empty();
			$('#txt_model').append('<option value=0>' +'---None---' +'</option>');
			$('#txt_model').val(0)
		}
		else{
			jQuery.ajax({type: "GET",
			url:'/Search',
			data: {'value':mname,
					'isactive': true},
			dataType: 'json',
			success: function (response){
				$('#txt_model').empty();
				$('#txt_model').append('<option value="">' +'---None---' +'</option>');
				for (var index = 0; index < response.selected_car_models.length; index++) {
      				$('#txt_model').append('<option value="' + response.selected_car_models[index][0] + '">' + response.selected_car_models[index][2] + '</option>');
   				}
			}
		});
	  }
	});
	
	$("#txt_model").change(function(){
		let modame = $('#txt_manufacturer').val()
		let e = document.getElementById('txt_model')
		let model_name = e.options[e.selectedIndex].text;
		let request = new Request("static/Car_Color.json");
		fetch(request)
			.then(function(response){
				return response.json()
			})
			.then(function(data){
				$('#txt_color').empty();
				$('#txt_color').append('<option value="">' +'---None---' +'</option>');
				for (var index = 0; index < data[model_name].length; index++) {
      				$('#txt_color').append('<option value="' + data[model_name][index] + '">' + data[model_name][index] + '</option>');
   				}
			})
	});
	
	
	$("#txtCarSearch").keyup(function(event){
		let searchText = event.target.value
			clearFilters()
			if(searchText != ''){
				jQuery.ajax({type: "GET",
					url:'/CarDetails',
					data: {'searchText':searchText},
					dataType: 'json',
					success: function (response){
    					wishlisted_car_ids_set = getWishlistedCars(response.wishlisted_cars)
    					displayData(response.car_list,wishlisted_car_ids_set,response.sessionvar)
					}
				});
			}
			else{
				jQuery.ajax({type: "GET",
					url:'/CarDetails',
					dataType: 'json',
					success: function (response){
    					wishlisted_car_ids_set = getWishlistedCars(response.wishlisted_cars)
    					displayData(response.car_list,wishlisted_car_ids_set,response.sessionvar)
					}
				});
			}
	});
	
	/* Method to validate date of birth on user signup */
	$("#txt_dob").change(function(event){
		let dob = new Date(event.target.value)
		jQuery.ajax({type: "GET",
			url:'/GetCurrentDate',
			dataType: 'json',
			success: function (response){
				let utctime = response.result + " UTC"
				let todaydate = new Date(new Date(utctime).toISOString().slice(0, 10))
				if(todaydate < dob){
					$('#invalid_dob_div').html('Date of birth cannot be in future')
					document.getElementById('txt_dob').setCustomValidity('Date of birth cannot be in future')
				}
				else{
					let ageval = Math.abs(todaydate - dob)/(1000*3600*24)/365
					if(ageval < 18){
						$('#invalid_dob_div').html('You must be above 18 years to sign up')
						document.getElementById('txt_dob').setCustomValidity('You must be above 18 years to sign up')
					}
					else{
						document.getElementById('txt_dob').setCustomValidity('')
						$('#invalid_dob_div').html('')
					}
				}
			}
		});
	});
	
	/* Display spinner when page loads */
	 var $loading = $('#spinnerDiv').hide();
	$(document)
		.ajaxStart(function () {
			$loading.show();
		})
		.ajaxStop(function () {
			$loading.hide();
		});
		
	  $("#txt_manufacturerlist").change(function(){
		let mname = $('#txt_manufacturerlist').val()
		if(mname == ''){
			$('#txt_modellist').empty();
			$('#txt_modellist').append('<option value="">' +'---None---' +'</option>');
			$('#txt_modellist').val('')
			$('#txt_modal_status').empty();
			$('#txt_modal_status').append('<option value="">' +'---None---' +'</option>');
			$('#txt_modal_status').val('')
			$('#txt_body_color').empty()
			$('#bodycolor-div').addClass('hide-element')
			$('#addBodyColorBtn').addClass('hide-element')
		}
		else{
			getModelList(mname,null)
	  }
	});
	
	$("#txt_modellist").change(function(){
		let mname = $('#txt_modellist').val()
		let e = document.getElementById('txt_modellist')
		let model_name = e.options[e.selectedIndex].text;
		let status = mname.split('_')[1]
		$('#txt_modal_status').empty();
		$('#txt_modal_status').append('<Option value="true">Active</Option><Option value="false">Inactive</Option>');
		if(mname == ''){
			$('#bodycolor-div').addClass('hide-element')
			$('#addBodyColorBtn').addClass('hide-element')
		}
		else{
			let request = new Request("static/Car_Color.json");
			fetch(request)
				.then(function(response){
					return response.json()
				})
				.then(function(data){
					$('#bodycolor-div').removeClass('hide-element')
					$('#addBodyColorBtn').removeClass('hide-element')
					$('#txt_body_color').empty()
					for (var index = 0; index < data[model_name].length; index++) {
      					$('#txt_body_color').append(data[model_name][index]+'<br/>');
   					}
				})
		}
		if(status == 'true'){
			$('#txt_modal_status').val(status)
		}
		else if(status == 'false'){
			$('#txt_modal_status').val(status)
		}
		else{
			$('#txt_modal_status').empty();
			$('#txt_modal_status').append('<option value="">' +'---None---' +'</option>');
			$('#txt_modal_status').val('')
		}
	});
	
	$("#txt_manufacturer_name").change(function(){
		let mname = $('#txt_manufacturer_name').val()
		if(mname == ''){
			$('#txt_new_Manufacturer').removeAttr('disabled')
		}
		else{
			$('#txt_new_Manufacturer').attr('disabled','true')
			$("#txt_new_Manufacturer").val('')
		}
	});
	
	$("#txt_modal_status").change(function(){
		let modelFormData = new FormData()
		modelFormData.append("form",$('#update_status_form').serialize())
		modelFormData.append("actiontType", "MODEL_UPDATE")
		jQuery.ajax({type: "POST",
			url:'/admin',
			data: modelFormData,
			contentType: false,
			processData: false,
			dataType: 'json',
			success: function (response){
				if(typeof(response) == 'object' && response['result'] == 'SUCCESS'){
					let mname = $('#txt_manufacturerlist').val()
					let modelid = $("#txt_modellist").val().split('_')[0]+'_'+$("#txt_modal_status").val()
					getModelList(mname,modelid)		
				}
			}
		}); 
	});
	
	$("#txtUserSearch").keyup(function(event){
		if(event.code == 'Enter'){
			let searchText = event.target.value
			jQuery.ajax({
    			type: "GET",
				url:'/SearchAndUpdateRecords',
				data : {'value':searchText,
				        'table_name':'user'},
				dataType: 'json',
					success: function (response){
						if(typeof(response) == 'object' && 'ERROR' in response){
  							$('#user-search-errordiv').html(response['ERROR'])	
						}
						else if(response.result == null){
							$('#user-search-errordiv').removeClass("hide-element")
							$('#user-search-errordiv').html('No user profile found!')
							$('#user-profile-div').addClass("hide-element")
						}
						else{
							$('#user-search-errordiv').addClass("hide-element")
							$('#user-profile-div').removeClass('hide-element')
							$('#txt_userfirstname').val(response.result[0][0])
							$('#txt_userlastname').val(response.result[0][1])
							$('#txt_useremail_id1').val(response.result[0][2])
							$('#txt_userphone_no').val(response.result[0][3])
							$('#txt_userId').val(response.result[0][11])
						}
					}
			});		
		}
	});
	
	function getModelList(mname,modelid){
		jQuery.ajax({type: "GET",
			url:'/Search',
			data: {'value':mname,
					'isactive': false},
			dataType: 'json',
			success: function (response){
				$('#txt_modellist').empty();
				$('#txt_modellist').append('<option value="">' +'---None---' +'</option>');
				for (var index = 0; index < response.selected_car_models.length; index++) {
					if(response.selected_car_models[index][3]==true)
      					$('#txt_modellist').append('<option value="' + response.selected_car_models[index][0]+'_'+response.selected_car_models[index][3] + '">' + response.selected_car_models[index][2] + '</option>');
      				else
      					$('#txt_modellist').append('<option style="color:red" value="' + response.selected_car_models[index][0]+'_'+response.selected_car_models[index][3] + '">' + response.selected_car_models[index][2] + '</option>');
   				}
   				if(modelid!=null){
   					$("#txt_modellist").val(modelid)
   				}
			}
		});
	}
});
