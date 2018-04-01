readData().then((snapshot) => {
	snapshot.forEach((child) => {
		const key = child.key
		const data = child.val()

		cardBody = ($('<div class="card-body"></div>'))

		cardBody.append($('<h3 class="sans-serif">Spring 2018 \> Psychology</h3>'))
		cardBody.append($('<h1>'+data.title+'</h1>'))

		card2 = ($('<div class="card"></div>'))
		card2.append(cardBody)
		$("#notes-list").append($('<div class="p-2 col-sm-4"></div>').append(card2))
	})
})
