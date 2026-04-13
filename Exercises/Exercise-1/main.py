import requests
import aiohttp
import zipfile
import os
import asyncio

os.makedirs('downloads', exist_ok=True)

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

async def download_file(url:str, session: aiohttp.ClientSession) -> None:
    try:
        file_name = url.split("/")[-1]
        file_path = 'downloads' + "//" + file_name
        async with session.get(url) as response:
            if response.status == 200:
                with open(file_path, 'wb') as f:
                    async for chunk in response.content.iter_chunked(8192):
                        f.write(chunk)
            else:
                print(f"Some thing wrong with the zip file {file_name}, detail: {response.status}")
        print(f"Successfully download zip file {file_name}")
    except Exception as e:
        print(f"Failed to download zip file {file_name}, detail: {e}")

def extract_csv(file_list: list) -> None:

async def main():
    async with aiohttp.ClientSession() as session:
        task = [download_file(url = uri, session = session) for uri in download_uris]
        await asyncio.gather(*task)


if __name__ == "__main__":
    asyncio.run(main())
