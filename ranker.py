def rank_candidates(df):

    ranked = df.sort_values(
        by="Final_Score",
        ascending=False
    )

    ranked.reset_index(
        drop=True,
        inplace=True
    )

    ranked.index = ranked.index + 1

    return ranked