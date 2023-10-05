from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/recommendations/v1/{user_id}")
async def get_recommendations(request: Request, user_id: int):
    try:
        data = await request.json()
        content_seen = data.get('content_seen', [])

        recommendations = [idx * 2 for idx in content_seen]

        return {'user_id': user_id, 'recommendations': recommendations}

    except Exception as e:
        return {'error': str(e)}
