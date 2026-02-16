import json

def load_data():
    try:
        with open('youtube_videos.txt', 'r') as file:
            videos = json.load(file)
            #print(type(videos))
            return videos
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube_videos.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 50)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({
        'name': name,
        'time': time,
    })
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index-1] = {
            'name': name,
            'time': time,
        }
        save_data_helper(videos)
    else:
        print("Invalid  video index. Please try again.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid  video index. Please try again.")

def main():
    videos = load_data()
    while True:
        print("\n YouTube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video ")
        print("5. Exit the application")
        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting the application")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
