from fetch.job import Job




job = Job()
job.browserOpen()
job.fetch("nzherald")
# job.fetch(stuff)
# job.fetch(newshub)
# job.fetch(newsZB)
# job.fetch(oneNews)
job.browserClose()
