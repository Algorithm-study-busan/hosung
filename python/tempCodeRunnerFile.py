while in_range(nr+dr[i], nc+dc[i]) :
                if board[nr][nc] != 0 :
                    break
                nr += dr[i] 
                nc += dc[i]
            if visited[nr][nc] == -1 :
                visited[nr][nc] = visited[cr][cc] + 1
                q.append([nr,nc])