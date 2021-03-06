const $flavor = $('#flavor');
const $size = $('#size');
const $rating = $('#rating');
const $image = $('#image');
const $submitButton = $('#submit-button');
const $cupcakeList = $('#cupcake-list');

$submitButton.click(addCupcake);

async function addCupcake() {
	API_URL = '/api/cupcakes';

	data = {
		flavor : $flavor.val(),
		size   : $flavor.val(),
		rating : $rating.val(),
		image  : $image.val()
	};

	const response = await axios.post(API_URL, data);

	const cupcake = response.data.cupcake;

	const $new_cupcake = $(
		`<div class="card mb-3 border rounded border-info shadow" style="width: 300px; height: 151px;"><div class="row g-0"><div class="col-md-4 cupcake_picture_div"><img src="${cupcake.image}" alt="${cupcake.flavor}" class="cupcake_picture"></div><div class="col-md-8"><div class="card-body"><h5 class="card-title">${cupcake.flavor}</h5><p class="card-text"><b>Size:</b> ${cupcake.size}</p><p class="card-text"><b>Rating:</b> ${cupcake.rating}</p></div></div></div></div>`
	);
	$new_cupcake.appendTo($cupcakeList);
}
