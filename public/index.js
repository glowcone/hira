var postKey;
readData().on('value', (snapshot) => {
		$("#notes-list").empty()
	snapshot.forEach((child) => {
		const key = child.key
		const data = child.val()

		cardBody = ($('<div class="card-body"></div>'))

		cardBody.append($('<h3 class="sans-serif">Spring 2018 \> Psychology</h3>'))
		cardBody.append($('<h1>'+data.title+'</h1>'))

		card2 = ($('<a href="#" class="card"></a>'))
		card2.click((e) => {
			e.preventDefault()
			localStorage.setItem('noteTitle', data.title)
			localStorage.setItem('noteTranscript', data.transcript)
			postKey = key
			location.href = '/view-note'
		})
		card2.append(cardBody)
		$("#notes-list").append($('<div class="p-2 col-md-4"></div>').append(card2))
	})
})
