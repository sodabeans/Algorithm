def solution(genres, plays):
    answer = []
    total_play = {}
    each_genre = {}
    
    for idx in range(len(genres)):
        curr_genre = genres[idx]
        curr_play = plays[idx]
        if curr_genre in total_play:
            total_play[curr_genre] += curr_play
        else:
            total_play[curr_genre] = curr_play

        if curr_genre not in each_genre:
            each_genre[curr_genre] = [(curr_play, idx)]
            continue
        else:
            each_genre[curr_genre].append((curr_play, idx))

    total_play = sorted(total_play.items(), key=lambda item: item[1], reverse=True)
    for genre, _ in total_play:
        each_genre[genre] = sorted(each_genre[genre], key=lambda item: item[0], reverse=True)
        answer.append(each_genre[genre][0][1]) 
        if len(each_genre[genre]) > 1:
            answer.append(each_genre[genre][1][1]) 
    
    return answer
  
