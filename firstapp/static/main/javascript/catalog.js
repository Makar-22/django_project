const elastic = document.querySelector('#elastic')

            elastic.addEventListener('input', (ev) => {
                const value = ev.target.value.trim()
                const elasticItems = document.querySelectorAll('.dropdown')
                const searchRegExp = new RegExp(value, 'gi')

                if (value === '') {
                    elasticItems.forEach((el) => {
                        el.classList.remove('hide')
                    })
                    return
                }

                elasticItems.forEach((el) => {
                    const innerCard = el.querySelector('.dropbtncommon')
                    const elementText = innerCard.textContent
                    const isContainsSearchRequest = searchRegExp.test(elementText)
                    if (!isContainsSearchRequest) {
                        el.classList.add('hide')
                    } else {
                        el.classList.remove('hide')
                    }
                })
            })