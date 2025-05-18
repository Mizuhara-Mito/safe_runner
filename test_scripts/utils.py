def on_fail(e):
    print(f"[TEST FAIL] Caught exception: {type(e).__name__} - {e}")
